from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USER :str = 'root'
    DB_PASSWORD:str = 'root'
    DB_HOST:str = 'localhost'
    DB_PORT:str = '3306'
    DB_NAME:str = 'users'
    SECRET_KEY:str = "Aditya"
    ALGORITHM:str = "HS256"
    EXPIRATION_TIME:int = 1


    class Config:
        env_file= ".env"


envObj= Settings()