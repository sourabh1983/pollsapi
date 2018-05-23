from django.urls import path

from .views import PollList, PollDetail, ChoiceList, CreateVote, ChoiceDetail

app_name = 'polls'

urlpatterns = [
    path("", PollList.as_view(), name="polls_list"),
    path("<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:poll_pk>/choices/<int:pk>/", ChoiceDetail.as_view(), name="choice_detail"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]