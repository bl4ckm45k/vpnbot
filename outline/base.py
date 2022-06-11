import asyncio
import logging
from typing import Optional, Union, Dict, List

import aiohttp
import ujson as json

from .api import make_request, Methods

logger = logging.getLogger(__name__)


class OutlineManager:
    def __init__(self, api_url: str,
                 loop: Optional[Union[asyncio.BaseEventLoop, asyncio.AbstractEventLoop]] = None,
                 connections_limit: int = None,
                 timeout: Optional[Union[int, float, aiohttp.ClientTimeout]] = None, ):
        self.headers = {'Content-Type': 'application/json'}
        self._api_url = api_url
        self._main_loop = loop

        self._session: Optional[aiohttp.ClientSession] = None
        self.timeout = timeout

    async def get_new_session(self) -> aiohttp.ClientSession:
        return aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(verify_ssl=False),
            json_serialize=json.dumps
        )

    @property
    def loop(self) -> Optional[asyncio.AbstractEventLoop]:
        return self._main_loop

    async def get_session(self) -> Optional[aiohttp.ClientSession]:
        if self._session is None or self._session.closed:
            self._session = await self.get_new_session()

        if not self._session._loop.is_running():
            await self._session.close()
            self._session = await self.get_new_session()

        return self._session

    def session(self) -> Optional[aiohttp.ClientSession]:
        return self._session

    async def close(self):
        """
        Close all client sessions
        """
        if self._session:
            await self._session.close()

    async def request(self, method: str,
                      data: Optional[Dict] = None, post: bool = False, **kwargs) -> Union[List, Dict, bool]:
        """
        Make an request to ABCP API

        :param method: API method
        :type method: :obj:`str`
        :param data: request parameters
        :param post:
        :type data: :obj:`dict`
        :return: result
        :rtype: Union[List, Dict]
        :raise: :obj:`utils.exceptions`
        """

        return await make_request(await self.get_session(), self._api_url,
                                  method, data, post, timeout=self.timeout, **kwargs)

    async def create_key(self):
        return await self.request(Methods.KEYS, None, True)

    async def delete_key(self, key_id: int):
        return await self.request(Methods.KEYS + f"/{key_id}")
