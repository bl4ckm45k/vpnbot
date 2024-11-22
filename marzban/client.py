import asyncio
import base64
import json
import logging
from datetime import datetime, timedelta
from typing import List, Optional
from urllib.parse import urlparse, parse_qs

from marzban_api_client.api.user import add_user, get_user, delete_expired_users
from marzban_api_client.models import UserCreate, UserCreateProxies, UserResponse
from marzban_api_client.types import Response

from loader import marzban_client

logger = logging.getLogger(__name__)
proxies = {
    "vless": {
        "flow": ""
    }
}
proxies = UserCreateProxies.from_dict(proxies)


def expire_timestamp(expire: datetime):
    new_utc_timestamp = int(expire.timestamp())
    return new_utc_timestamp


async def create_user(sub_id: str, expire: datetime) -> bool:
    exp_timestamp = expire_timestamp(expire)
    user_data = UserCreate(
        username=sub_id,
        expire=exp_timestamp,
        proxies=proxies)
    response: Response = add_user.sync_detailed(client=await marzban_client.get_client(), body=user_data)
    logger.info(f'Create user result: {response.status_code}')
    if not response:
        return False
    return True


async def get_marz_user(sub_id: str) -> UserResponse:
    response: Response = await get_user.asyncio_detailed(sub_id,
                                                         client=await marzban_client.get_client())
    if not response.parsed:
        await create_user(sub_id, expire=datetime.now() + timedelta(days=365 * 10))
        await asyncio.sleep(1)
        return await get_marz_user(sub_id)
    return response.parsed


async def get_user_links(sub_id: str) -> str:
    response: UserResponse = await get_marz_user(sub_id)
    keys = []
    for x in response.links:
        key_data = x.split('://')
        if key_data[0] == 'vmess':
            data = json.loads(base64.b64decode(key_data[1]).decode('utf-8'))
            keys.append(
                'Протокол: <b>{protocol_type}</b>\nКлюч: <pre>{access_key}</pre>'
                .format(protocol_type=f'VMESS {data["net"]}', access_key=x)
            )
        elif (key_data[0] == 'vless') or (key_data[0] == 'trojan'):
            parsed_url = urlparse(x)
            if key_data[0] == 'vless':
                query_params = parse_qs(parsed_url.query)
                keys.append(
                    'Протокол: <b>{protocol_type}</b>\nКлюч: <pre>{access_key}</pre>'
                    .format(protocol_type=f'VLESS {query_params["type"][0]}', access_key=x)
                )
            if key_data[0] == 'trojan':
                keys.append(
                    'Протокол: <b>{protocol_type}\n</b>Ключ: <pre>{access_key}</pre>'
                    .format(protocol_type=f'Trojan WS', access_key=x)
                )
        elif key_data[0] == 'ss':
            keys.append(
                'Протокол <b>{protocol_type}\n</b>Ключ: \n<pre lang="vpn">{access_key}</pre>'.format(
                    protocol_type='Shadowsocks', access_key=x))
    return "\n\n".join(keys)


async def delete_users():
    local_utc_time = datetime.utcnow()
    response: Response = await delete_expired_users.asyncio_detailed(expired_before=local_utc_time,
                                                                     client=await marzban_client.get_client())
    logger.info(f'DELETE USERS RESPONSE: {response.parsed}')
