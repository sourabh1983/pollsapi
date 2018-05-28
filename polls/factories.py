import datetime
import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from polls.models import Poll, Choice


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        # django_get_or_create = ('username', 'email', 'password')

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)


class PollFactory(DjangoModelFactory):

    class Meta:
        model = Poll

    question = factory.Sequence(lambda n: 'Poll {}'.format(n))
    created_by = factory.SubFactory(UserFactory)
    pub_date = factory.LazyFunction(datetime.datetime.now)


class ChoiceFactory(DjangoModelFactory):

    class Meta:
        model = Choice

    poll = factory.SubFactory(PollFactory)
    choice_text = factory.Sequence(lambda n: 'Choice {}'.format(n))
