import requests
import time

BASE_API_URL = "https://stellarburgers.education-services.ru/api"
TIMEOUT = 40


def _request_with_retry(method, url, attempts=3, **kwargs):
    for attempt in range(attempts):
        try:
            return requests.request(method, url, timeout=TIMEOUT, **kwargs)
        except (requests.ConnectTimeout, requests.ReadTimeout):
            if attempt == attempts - 1:
                raise
            time.sleep(2)
            
class StellarBurgersAPI:
    @staticmethod
    def register_user(email: str, password: str, name: str) -> requests.Response:
        return requests.post(
            f"{BASE_API_URL}/auth/register",
            json={"email": email, "password": password, "name": name}, timeout=15
        )

    @staticmethod
    def delete_user(access_token: str) -> requests.Response:
        return requests.delete(
            f"{BASE_API_URL}/auth/user",
            headers={"Authorization": access_token}, timeout=15
        )
