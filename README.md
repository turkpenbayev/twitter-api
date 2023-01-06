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
        },
        {
            "tweet_id": "1611128483547348992",
            "text": "Some habits are hard to break lol.  Maybe I should just get bulletproof shoes."
        },
        {
            "tweet_id": "1611112185895473163",
            "text": "Ouch my feet!! https://t.co/4pqBY6rZDu"
        },
        {
            "tweet_id": "1611111410846814208",
            "text": "@cb_doge @MrAndyNgo @josephmenn @ExplainThisBob Will do. He is a good bot."
        },
        {
            "tweet_id": "1611110531917828097",
            "text": "@MrAndyNgo @josephmenn Joseph Menn is a contemptible liar. Twitter policy has always been to suspend accounts that clearly &amp; repeatedly incite violence."
        },
        {
            "tweet_id": "1611047137705603072",
            "text": "RT @Tesla: Tesla’s impact in California → https://t.co/4MudoNiCJG"
        },
        {
            "tweet_id": "1611044282030518272",
            "text": "@jonastyle_ Journalists should do shots every time there is a negative article about me …"
        },
        {
            "tweet_id": "1611035401225113600",
            "text": "Elon Musk should"
        },
        {
            "tweet_id": "1611034662301995010",
            "text": "Subtle, but I am beginning to suspect opinions differ on this matter …\n\nIf not McCarthy, then seriously who?"
        }
    ]

