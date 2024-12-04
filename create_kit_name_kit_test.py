import pytest
from sender_stand_request import get_new_user_token, post_new_client_kit
from data import get_kit_body

@pytest.fixture
def auth_token():
    return get_new_user_token()

def positive_assert(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_name_length_1(auth_token):
    positive_assert(get_kit_body("a"), auth_token)

def test_name_length_511(auth_token):
    positive_assert(get_kit_body("a" * 511), auth_token)

def test_name_empty(auth_token):
    negative_assert_code_400(get_kit_body(""), auth_token)

def test_name_length_512(auth_token):
    negative_assert_code_400(get_kit_body("a" * 512), auth_token)

def test_name_special_characters(auth_token):
    positive_assert(get_kit_body("!@#$%^&*"), auth_token)

def test_name_spaces(auth_token):
    positive_assert(get_kit_body(" A B "), auth_token)

def test_name_numbers(auth_token):
    positive_assert(get_kit_body("123456"), auth_token)

def test_name_missing(auth_token):
    negative_assert_code_400({})
