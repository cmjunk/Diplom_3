import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_API_URL = "https://stellarburgers.education-services.ru/api"
TIMEOUT = 40


def _request(method, url, **kwargs):
    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=1,
        allowed_methods=frozenset(["POST", "DELETE"]),
    )
    with requests.Session() as session:
        session.mount("https://", HTTPAdapter(max_retries=retry))
        return session.request(method, url, timeout=TIMEOUT, **kwargs)


class StellarBurgersAPI:
    @staticmethod
    def register_user(email: str, password: str, name: str) -> requests.Response:
        return _request(
            "POST", f"{BASE_API_URL}/auth/register",
            json={"email": email, "password": password, "name": name},
        )

    @staticmethod
    def delete_user(access_token: str) -> requests.Response:
        return _request(
            "DELETE", f"{BASE_API_URL}/auth/user",
            headers={"Authorization": access_token},
        )
