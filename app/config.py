import os
import pytz
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    TWITTER_API_URL: str = 'https://api.twitter.com'
    TWITTER_API_BEARER_TOKEN: str = 'AAAAAAAAAAAAAAAAAAAAADFbbgEAAAAAgbDQ72%2BKSSj4LUlfXndxsYyAs1c%3D7rYx14Ozbpzl7dJF4DkCsWxj198YKHM60emOl7bDtZhO24TQ4h'

    SERVICE_NAME: str = 'Twitter API'
    SERVICE_HOST: str = '0.0.0.0'
    SERVICE_PORT: int = 8000

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG: bool = False
    SHOW_DOCS: bool = True

    TIMEZONE = pytz.timezone('Asia/Almaty')

    class Config:
        case_sensitive = True
        env_file='env/app'


settings = Settings()
