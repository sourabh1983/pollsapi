from django.contrib import admin
from django.urls import include, path

from polls.views import CreateUser, HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('users/', CreateUser.as_view(), name='create_user'),
    path('', HomeView.as_view(), name='home'),
]
