import pytest

from words.models import User


@pytest.fixture
def user():
    return User.objects.create_user(
        username='TestUser', password='1234567', email='test@test.ru'
    )


@pytest.fixture
def user_client(user, client):
    client.force_login(user)
    return client
