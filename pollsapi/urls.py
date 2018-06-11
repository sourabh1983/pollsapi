from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from polls.views import CreateUser, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('users/', CreateUser.as_view(), name='create_user'),
    path('', serve, kwargs={'path': 'frontend/index.html'}),
    re_path(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/frontend/%(path)s', permanent=False)),
]
