import base64
import copy
import logging
import secrets

from marzban_api_client.api.core import get_core_config, modify_core_config
from marzban_api_client.models import GetCoreConfigResponseGetCoreConfigApiCoreConfigGet, ModifyCoreConfigPayload
from marzban_api_client.types import Response
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization
from loader import marzban_client


def generate_x25519_key() -> [x25519.X25519PrivateKey, str]:
    private_key = x25519.X25519PrivateKey.generate()
    # Получение raw приватного ключа
    private_key_raw = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,  # Используем raw формат
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()  # Нет шифрования
        # https://github.com/XTLS/Xray-core/blob/main/main/commands/all/x25519.go
    )

    # Преобразование ключей в Base64 (URL-safe)
    private_key_base64 = base64.urlsafe_b64encode(private_key_raw).decode('utf-8').rstrip("=")

    return private_key_base64, secrets.token_hex(8)


async def get_config():
    response: Response = await get_core_config.asyncio_detailed(client=await marzban_client.get_client())
    core_config: GetCoreConfigResponseGetCoreConfigApiCoreConfigGet = response.parsed
    return core_config.additional_properties
async def generate_config():
    xray_config = await get_config()
    have_new_settings = False
    existing_inbounds = xray_config['inbounds']
    new_inbounds = []
    for inbound in existing_inbounds:
        new_inbound = copy.deepcopy(inbound)
        if "streamSettings" in inbound:
            if "realitySettings" in inbound["streamSettings"]:
                if new_inbound["streamSettings"]["realitySettings"]["privateKey"] == 'MMX7m0Mj3faUstoEm5NBdegeXkHG6ZB78xzBv2n3ZUA':
                    private_key, short_id = generate_x25519_key()
                    new_inbound["streamSettings"]["realitySettings"]["privateKey"] = private_key
                    new_inbound["streamSettings"]["realitySettings"]["shortIds"] = [short_id]
                    new_inbounds.append(new_inbound)
                    have_new_settings = True
    if have_new_settings:
        logging.info(f'We need to replace the private keys')
        xray_config['inbounds'] = new_inbounds
        data: ModifyCoreConfigPayload = ModifyCoreConfigPayload.from_dict(xray_config)
        response: Response = await modify_core_config.asyncio_detailed(client=await marzban_client.get_client(), body=data)
        if response.status_code != 200:
            raise KeyError(f'Failed to create inbounds')
    logging.info(f'Генерация конфига завершена успешно')