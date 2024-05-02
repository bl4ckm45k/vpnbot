from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_id: int

    @staticmethod
    def from_env(env: Env):
        token = env.str("BOT_TOKEN")
        admin_id = env.int("ADMIN")

        return TgBot(token=token, admin_id=admin_id)


@dataclass
class Webhook:
    url: str
    domain: str
    use_webhook: bool

    @staticmethod
    def from_env(env: Env):
        url = env.str('SERVER_URL')
        domain = env.str('DOMAIN')
        use_webhook = env.bool('USE_WEBHOOK')
        return Webhook(url=url, domain=domain, use_webhook=use_webhook)


@dataclass
class Marzban:
    username: str
    password: str
    token_expire: int
    verify_ssl: bool

    @staticmethod
    def from_env(env: Env, env_marz: Env):
        username = env_marz.str("SUDO_USERNAME")
        password = env_marz.str("SUDO_PASSWORD")
        token_expire = env_marz.int("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 1440)
        verify_ssl = env.bool("MARZ_HAS_CERTIFICATE")
        return Marzban(username=username, password=password,
                       token_expire=token_expire,
                       verify_ssl=verify_ssl)


@dataclass
class Config:
    tg_bot: TgBot
    webhook: Webhook
    marzban: Marzban


def load_config():
    from environs import Env
    env = Env()
    env.read_env('.env')
    env_marz = Env()
    env_marz.read_env('.env.marzban')
    return Config(
        tg_bot=TgBot.from_env(env),
        webhook=Webhook.from_env(env),
        marzban=Marzban.from_env(env, env_marz)
    )
