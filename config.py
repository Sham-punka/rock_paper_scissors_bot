from dataclasses import dataclass
import os
import dotenv

dotenv.load_dotenv()


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    return Config(tg_bot=TgBot(token=os.getenv('BOT_TOKEN')))