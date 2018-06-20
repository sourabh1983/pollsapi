from django.contrib import admin
from django.urls import include, path, re_path

from polls.views import CreateUser, HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('users/', CreateUser.as_view(), name='create_user'),
    re_path(r'^.*$', HomeView.as_view(), name='home'),
]
