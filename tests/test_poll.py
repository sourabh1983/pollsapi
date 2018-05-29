import json

import pytest
from django.urls import reverse
from rest_framework import status

from polls.factories import PollFactory


@pytest.mark.django_db()
def test_get_poll_list_returns_expected_results(client, django_user_model):
    user = get_test_user_login(client, django_user_model)
    PollFactory(created_by=user)
    url = reverse('polls:polls_list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_create_poll(client, django_user_model):
    user = get_test_user_login(client, django_user_model)
    data = {'question': 'test poll question', 'created_by': user.id}
    url = reverse('polls:polls_list')
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED
    poll = response.json()
    assert 'id' in poll
    assert 'choices' in poll
    assert 'question' in poll
    assert 'pub_date' in poll
    assert 'created_by' in poll


def get_test_user_login(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password, email='test@test.com')
    client.login(username=username, password=password)
    return user
