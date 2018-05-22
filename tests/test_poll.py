import pytest
from django.urls import reverse
from polls.factories import PollFactory


@pytest.mark.django_db()
def test_post_returns_expected_results(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create(username=username, password=password, email='test@test.com')
    client.login(username=username, password=password)
    poll = PollFactory(created_by=user)
    url = reverse('polls:polls_list')
    response = client.get(url)
    assert response.status_code == 200
