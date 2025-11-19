import os
from typing import Optional

class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "7147525162:AAEWxgnuR1SIxwxX37rYZ761WVyal6njAC8")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "https://youdomain.com/webhook")
    SECRET_TOKEN: str = os.getenv("SECRET_TOKEN", "you_secret_token")

settings = Settings()