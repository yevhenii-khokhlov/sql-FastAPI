from pydantic import BaseSettings


def get_settings():
    return Settings()


class Settings(BaseSettings):
    app_name: str = "sql-FastAPI"
    db_username: str
    db_database: str
    db_server: str
    db_password: str
    api_token: str
    memcachier_servers: str
    memcachier_username: str
    memcachier_password: str

    class Config:
        env_file = ".env"
