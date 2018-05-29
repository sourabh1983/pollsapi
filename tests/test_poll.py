import json

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from polls.factories import ChoiceFactory, PollFactory


@pytest.mark.django_db()
def test_get_poll_list_returns_expected_results(client, django_user_model):
    user = get_test_user_login(client, django_user_model)
    PollFactory(created_by=user)
    url = reverse('polls:polls_list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_get_choice_list_returns_expected_results(client, django_user_model):
    get_test_user_login(client, django_user_model)
    choice = ChoiceFactory()
    url = reverse('polls:choice_list', kwargs={'pk': choice.poll.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    choice = response.json()
    assert 'id' in choice[0]
    assert 'votes' in choice[0]
    assert 'choice_text' in choice[0]
    assert 'poll' in choice[0]


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


@pytest.mark.django_db()
def test_poll_choice_can_be_edited_by_creator(client, django_user_model):
    tom1 = get_test_user_login(client, django_user_model, 'tom1', 'tom1')
    tom2 = get_test_user_login(client, django_user_model, 'tom2', 'tom2')
    token = Token.objects.create(user=tom2)
    poll1 = PollFactory(created_by=tom1)
    url = reverse('polls:choice_list', kwargs={'pk': poll1.id})
    data = {'poll': poll1.id, 'choice_text': 'poll1 choice'}
    header = {'Authorization': 'Token ' + str(token)}
    response = client.post(
        url,
        json.dumps(data),
        content_type='application/json',
        header=header
    )
    response.status_code = status.HTTP_403_FORBIDDEN


def get_test_user_login(client, django_user_model, username='user1', password='bar'):
    user = django_user_model.objects.create_user(username=username, password=password, email='test@test.com')
    client.login(username=username, password=password)
    return user
