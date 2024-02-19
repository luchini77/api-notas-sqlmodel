import os
import secrets
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = 'Tareas-Fastapi'
    PROJECT_VERSION:str ='1.0.0'

    DATABASE:str = os.getenv('SQLITE')
    #POSTGRES_DB:str = os.getenv('POSTGRES_DB')
    # POSTGRES_USER:str = os.getenv('POSTGRES_USER')
    # POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    # POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
    # POSTGRES_PORT:str = os.getenv('POSTGRES_PORT')

    # DATABASE_URL =f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = secrets.token_urlsafe(32)

    API_USERNAME: str = os.getenv('API_USERNAME')
    API_PASSWORD: str = os.getenv('API_PASSWORD')

    DATABASE_URL = f"{DATABASE}"


settings = Settings()