from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    def get_queryset(self):
        qs = super().get_queryset().filter(poll_id=self.kwargs.get('pk'))
        return qs

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs.get('pk'))
        if not request.user == poll.created_by:
            raise PermissionDenied('You can not create choice for this poll')
        return super().post(request, *args, **kwargs)


class ChoiceDetail(generics.RetrieveDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        qs = super().get_queryset().filter(
            poll_id=self.kwargs.get('poll_pk'),
            # pk=self.kwargs.get('choice_pk')
        )
        return qs

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs.get('poll_pk'))
        if not request.user == poll.created_by:
            raise PermissionDenied('You can not delete choice for this poll')
        return super().destroy(request, *args, **kwargs)

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer


class CreateUser(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)