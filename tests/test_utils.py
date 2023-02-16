import pytest

from app.utils.Utils import Utils
from app.entity.User import User

def test_user_to_json():
    user = User(1, 'User 1', 'user-1@gmail.com')
    user_json = Utils.convert_object_to_json(user)
    user_expected_json = { 'email': 'user-1@gmail.com', 'id': 1, 'username': 'User 1' }

    assert user_json == user_expected_json

def test_user_list_to_json():
    user_1 = User(1, 'User 1', 'user-1@gmail.com')
    user_2 = User(2, 'User 2', 'user-2@gmail.com')
    user_list = []
    user_list.append(user_1)
    user_list.append(user_2)

    user_json_list = Utils.convert_object_list_to_json(user_list)
    user_expected_json_list = [{ 'id': 1, 'username': 'User 1', 'email': 'user-1@gmail.com' }, { 'id': 2, 'username': 'User 2', 'email': 'user-2@gmail.com' }]

    print(user_json_list)
    print(user_expected_json_list)

    assert user_json_list == user_expected_json_list
