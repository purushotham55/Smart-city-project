from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    #if variables are not loaded from .env then it uses dummy variables
    WATSONX_API_KEY: str = "dummy_key"
    WATSONX_PROJECT_ID: str = "dummy_project"
    WATSONX_URL: str = "https://dummy.com"
    WATSONX_MODEL_ID: str = "ibm/granite-3-2b-instruct"
    PINECONE_API_KEY: str = "pcsk_3qJpjJ_LjqLgwz2ZFGiMQ3nss8UkSqc22xSeyyofoPDsQH4t29Pmfoj9jCNXTP68RGS7VT"
    PINECONE_ENV: str = "dummy_env"
    INDEX_NAME: str = "dummy_index"

    class Config:
        # Look for .env file in the project root (parent of app directory)
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        env_file_encoding = 'utf-8'
        extra = "ignore"  # This will ignore extra fields

settings = Settings() 