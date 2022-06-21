import logging
from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from config import load_config

logger = logging.getLogger(__name__)
c = load_config(".env")


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def execute(self, command, *args, fetch: bool = False, fetchval: bool = False, fetchrow: bool = False,
                      execute: bool = False):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(user=c.db.user,
                                                  password=c.db.password,
                                                  host=c.db.host,
                                                  database=c.db.database,
                                                  port=c.db.port
                                                  )
            logger.info(f'Создано подключение к БД')
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                return result

    async def get_servers(self):
        sql = "SELECT (id, country) FROM vpn_servers"
        return await self.execute(sql, fetch=True)

    async def get_server_key(self, server_id):
        sql = "SELECT api_link FROM vpn_servers WHERE id=$1"
        return await self.execute(sql, server_id, fetchval=True)
