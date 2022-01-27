from config import get_settings


settings = get_settings()


def is_token_valid(headers):
    api_token = headers.get('api_token', '')

    if api_token == settings.api_token:
        return True

    return False
