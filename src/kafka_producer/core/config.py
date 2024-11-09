from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Kafka environment variables
    KAFKA_SERVER: str
    KAFKA_TOPIC: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
