from dataclasses import dataclass
from typing import List


@dataclass
class DbConfig:
    host: str
    port: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]
    ip: str
    port: int


@dataclass
class Webhook:
    url: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    webhook: Webhook


def load_config():
    from environs import Env
    env = Env()
    env.read_env('.env')
    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=env.int("ADMIN"),
            ip=env.str('BOT_IP'), port=int(env.int("BOT_PORT"))
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            port=env.str('DB_PORT'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        webhook=Webhook(url=env.str("SERVER_URL"))
    )
