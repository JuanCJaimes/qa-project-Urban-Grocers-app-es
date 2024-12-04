import requests
from configuration import BASE_URL, CREATE_USER_ENDPOINT, CREATE_KIT_ENDPOINT

def get_new_user_token():
    response = requests.post(f"{BASE_URL}{CREATE_USER_ENDPOINT}")
    response.raise_for_status()
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(f"{BASE_URL}{CREATE_KIT_ENDPOINT}", json=kit_body, headers=headers)
    return response
