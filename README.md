# Сервис Twitter API

```sh
docker-compose up -d --build
```
## выполныние задачи

-  подготовить docker-compose для запуска всех сервисов проекта одной командой
-  по адресу /docs/ открывалась страница со Swagger UI и в нём отображалось описание разработанного API. Пример: [http://0.0.0.0:8000/docs/](http://0.0.0.0:8000/docs/)


**POST create parse session** - на входе список(не строка с разделителем!) ссылок на твиттер аккаунты (от 1 до 500): 

    Пример входных данных:

    [
    “https://twitter.com/tyler”,
    	“https://twitter.com/novogratz”,
    	“https://twitter.com/elonmusk”,
    	“https://twitter.com/MessariCrypto”,
    	“https://twitter.com/CryptoHayes”
    ]

    На выходе идентификатор по которому получаем статус парсинга каждого аккаунта из списка. Это значит, что по полученному идентификатору мы можем получить весь список входных данных из п.1 с текущим статусом парсинга.

    Пример: 
    {‘session_id’: 42}


**GET: /api/users/status** - Получение статуса парсинга всего списка аккаунтов из п.1 по полученному идентификатору session_id): 
    на входе идентификатор

    Пример:
    {‘session_id’: 42}

    на выходе список username и его статус парсинга

    Пример:
    [
        {
            ‘username’: ‘elonmusk’,
            ‘status’: ‘success’
        },
        {
            ‘username’: ‘tyler’,
            ‘status’: ‘pending’
        },
        {
            ‘username’: ‘test’,
            ‘status’: ‘failed’
        }
    ]


**GET: /api/user/{username}** - Получение данных твиттер аккаунта по его username:
    Получение данных твиттер аккаунта по его username
    Пример:
    {
        "twitter_id": "20128733",
        "username": "YLER",
        "name": "carley sinclair",
        "followers_count": 6,
        "following_count": 18,
        "description": ""
    }


**GET: /api/tweets/{twitter_id}** - Получение 10 последних твитов аккаунта по его twitter_id:
    на входе twitter_id, полученный при парсинге
    на выходе список твитов
    Пример:
    [
        {
            "tweet_id": "1611139320391544832",
            "text": "@lrocket Hi Tom!"
        },
        {
            "tweet_id": "1611138353705156609",
            "text": "@Hitch_Slapping @DrJBhattacharya True"
        }
    ]

