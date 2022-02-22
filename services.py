import uuid

import pylibmc

from config import get_settings


settings = get_settings()

mc = pylibmc.Client(
    [settings.memcachier_servers, ],
    binary=True,
    username=settings.memcachier_username,
    password=settings.memcachier_password,
    behaviors={
        # Faster IO
        'tcp_nodelay': True,

        # Keep connection alive
        'tcp_keepalive': True,

        # Timeout for set/get requests
        'connect_timeout': 2000,  # ms
        'send_timeout': 750 * 1000,  # us
        'receive_timeout': 750 * 1000,  # us
        '_poll_timeout': 2000,  # ms

        # Better failover
        'ketama': True,
        'remove_failed': 1,
        'retry_timeout': 2,
        'dead_timeout': 30,
    }
)


def is_token_valid(headers):
    api_token = headers.get('api_token', '')

    if api_token == settings.api_token:
        return True

    return False


def generate_response_id():
    return uuid.uuid4().hex[:16]


def get_response_by_id(response_id):
    response = mc.get(response_id)
    return response
