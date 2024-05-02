from datetime import datetime, timedelta
from typing import Optional

from marzban_api_client import AuthenticatedClient, Client
from marzban_api_client.api.admin import admin_token
from marzban_api_client.models.body_admin_token_api_admin_token_post import (
    BodyAdminTokenApiAdminTokenPost,
)


class MarzClientCache:
    def __init__(self, base_url: str, config, logger):
        self._client: Optional[AuthenticatedClient] = None
        self._exp_at: Optional[datetime] = None
        self._base_url: str = base_url
        self._config = config
        self._logger = logger
        self._token: str = ''

    async def get_client(self):
        if not self._client or self._exp_at < datetime.now():
            self._logger.info(f'Get new token')
            token = await self.get_token()
            self._token = token
            self._exp_at = datetime.now() + timedelta(minutes=self._config.marzban.token_expire - 1)
            self._client = AuthenticatedClient(
                base_url=self._base_url,
                token=self._token,
                verify_ssl=True
            )
            self._logger.info(f'Set new client object')
        self._logger.info(f'We have client object')
        return self._client

    async def get_token(self):
        try:
            login_data = BodyAdminTokenApiAdminTokenPost(
                username=self._config.marzban.username,
                password=self._config.marzban.password,
            )
            async with Client(base_url=self._base_url) as client:
                token = await admin_token.asyncio(
                    client=client,
                    body=login_data,
                )
                access_token = token.access_token
                return access_token
        except Exception as e:
            self._logger.error(f"Error getting token: {e}")
            raise
