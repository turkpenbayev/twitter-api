import abc
import typing
import dataclasses

import aiohttp
from app.config import settings
from app.services.twitter import exceptions


@dataclasses.dataclass()
class TwitterUserDTO:
    twitter_id: str
    username: str
    name: str
    followers_count: int
    following_count: int
    description: str


@dataclasses.dataclass()
class TweetDTO:
    id: str
    text: str


class TweeterAPIClient(abc.ABC):
    API_ROOT = settings.TWITTER_API_URL
    BASE_URL = '{api_root}/2/{path}'
    DEFAULT_HEADERS = {
        'Authorization': f'Bearer {settings.TWITTER_API_BEARER_TOKEN}'
    }

    def __init__(self, *args, **kwargs):
        self.session = aiohttp.ClientSession(
            headers=self.DEFAULT_HEADERS, trust_env=True)

    def get_timeout(self, timeout: typing.Union[int, typing.Tuple[int, int], None]):
        if isinstance(timeout, tuple):
            connect, read = timeout
            return aiohttp.ClientTimeout(sock_connect=connect, sock_read=read)
        else:
            return aiohttp.ClientTimeout(total=timeout)

    def make_url(self, path: str) -> str:
        return self.BASE_URL.format(
            api_root=self.API_ROOT,
            path=path
        )

    async def _get(
            self, url: str, timeout: typing.Union[int, typing.Tuple[int, int], None] = (1.0, 10.0), params: typing.Optional[typing.Dict] = None
    ) -> typing.Union[typing.Dict, typing.List]:
        try:
            async with self.session.get(url, timeout=self.get_timeout(timeout), params=params, ssl=False) as response:
                if response.status // 100 == 4:
                    raise exceptions.ServiceException(
                        status_code=response.status, message=response.reason, data=response.text)
                elif response.status // 100 == 5:
                    raise exceptions.ServiceException(
                        status_code=response.status, message=response.reason, data=response.text)
                response = await response.json()

                if response.get('errors', None) is not None:
                    raise exceptions.ServiceException(
                        status_code=200, message=response['errors'][0]['detail'], data=response)

                return response
        except aiohttp.ClientError as e:
            raise exceptions.RequestException() from e

    async def get_users_by_usernames(self, usernames: typing.List[str]) -> typing.Dict[str, TwitterUserDTO]:
        usernames_str = ','.join(usernames)
        path = 'users/by'
        params = {
            'usernames': usernames_str,
            'user.fields': 'id,name,username,description,public_metrics'
        }
        results = await self._get(url=self.make_url(path), params=params)
        try:
            return {
                item['username'].lower(): TwitterUserDTO(
                    item['id'],
                    item['username'],
                    item['name'],
                    item['public_metrics']['followers_count'],
                    item['public_metrics']['following_count'],
                    item['description']
                ) for item in results['data']
            }
        except KeyError:
            print(results)
            pass

    async def get_tweets_by_twitter_id(self, twitter_id: int) -> typing.List[TweetDTO]:
        path = f'users/{twitter_id}/tweets'
        params = {
            'max_results': 10,
            'tweet.fields': 'id,text'
        }
        results = await self._get(url=self.make_url(path), params=params)
        return [
            TweetDTO(
                item['id'],
                item['text']
            ) for item in results['data']
        ]
