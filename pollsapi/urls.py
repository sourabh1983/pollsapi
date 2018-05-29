from django.contrib import admin
from django.urls import include, path

from polls.views import CreateUser, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('users/', CreateUser.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
]
