from dataclasses import dataclass
from typing import List
from environs import Env


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
    use_redis: bool
    ip: str
    port: int


@dataclass
class TgChats:
    debug_chat: str


@dataclass
class Server:
    url: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    tg_chats: TgChats
    server: Server


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
            ip=env.str('BOT_IP'), port=env.int("BOT_PORT")
        ),
        tg_chats=TgChats(debug_chat=env.str('DEBUG_CHAT')),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            port=env.str('DB_PORT'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        server=Server(url=env.str("SERVER_URL"))
    )
