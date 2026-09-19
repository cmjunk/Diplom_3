import requests

BASE_API_URL = "https://stellarburgers.nomoreparties.site/api"


class StellarBurgersAPI:
    @staticmethod
    def register_user(email: str, password: str, name: str) -> requests.Response:
        return requests.post(
            f"{BASE_API_URL}/auth/register",
            json={"email": email, "password": password, "name": name},
        )

    @staticmethod
    def delete_user(access_token: str) -> requests.Response:
        return requests.delete(
            f"{BASE_API_URL}/auth/user",
            headers={"Authorization": access_token},
        )
