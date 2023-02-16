import pytest

from app.repository.UserRepository import UserRepository

def test_get_user_by_id():
    user_repository = UserRepository()
    user = user_repository.get_by_id(1)

    assert user.id == 1
    assert user.username == 'Usuario 1'
    assert user.email == 'usuario-1@gmail.com'

def test_get_user_by_id_with_id_not_existent():
    user_repository = UserRepository()
    user = user_repository.get_by_id(20)

    assert user == None

def test_get_all():
    user_repository = UserRepository()
    user = user_repository.get_all()
    assert len(user) > 0
