from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    version: str
    description: str

    model_config = SettingsConfigDict(env_file="config.env")

settings = Settings()
print(settings.app_name)
print(settings.version)
print(settings.description)
