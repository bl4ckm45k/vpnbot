import logging
from http import HTTPStatus

import aiohttp

from .exceptions import OutlineError, NetworkError

logger = logging.getLogger('Outline API')


def check_result(method_name: str, content_type: str, status_code: int, body):
    """
    Checks whether `result` is a valid API response.
    A result is considered invalid if:
    - The server returned an HTTP response code other than 200
    - The content of the result is invalid JSON.
    - The method call was unsuccessful (The JSON 'ok' field equals False)

    :param method_name: The name of the method called
    :param status_code: status code
    :param content_type: content type of result
    :param body: result body
    :return: The result parsed to a JSON dictionary
    :raises ApiException: if one of the above listed cases is applicable
    """
    logger.debug('Response for %s: [%d] "%r"', method_name, status_code, body)

    if content_type != 'application/json':
        raise NetworkError(f"Invalid response with content type {content_type}: \"{body}\"")
    if HTTPStatus.OK <= status_code <= HTTPStatus.IM_USED:
        return body
    elif status_code == HTTPStatus.BAD_REQUEST:
        raise OutlineError(f"{body} [{status_code}]")
    elif status_code == HTTPStatus.NOT_FOUND:
        raise OutlineError(f"{body} [{status_code}]")
    elif status_code == HTTPStatus.CONFLICT:
        raise OutlineError(f"{body} [{status_code}]")
    elif status_code in (HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN):
        raise OutlineError(f"{body} [{status_code}]")
    elif status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
        raise OutlineError(f"{body} [{status_code}]")

    raise OutlineError(f"{body} [{status_code}]")


async def make_request(session, url, method, post: bool = False, **kwargs):
    logger.info(f'Make request:'
                f'URL: {url}\n'
                f'Method: {method}\n')
    headers = {'Accept': 'application/json'}
    try:
        if post:
            async with session.post(f"{url}/{method}", headers=headers, **kwargs) as response:
                try:
                    body = await response.json()
                except:
                    body = response.text
                return check_result(method, response.content_type, response.status, body)
        else:
            async with session.delete(f"{url}/{method}", headers=headers, **kwargs) as response:
                if response.status == 204:
                    return True
                try:
                    body = await response.json()
                except:
                    body = response.text
                return check_result(method, response.content_type, response.status, body)
    except aiohttp.ClientError as e:
        raise NetworkError(f"aiohttp client throws an error: {e.__class__.__name__}: {e}")


class Methods:
    KEYS = 'access-keys'
