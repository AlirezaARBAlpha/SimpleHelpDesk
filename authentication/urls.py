from django.urls import path
from django.contrib.auth.views import LogoutView

from helpdesk import settings
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),

    path(r'^logout/$', LogoutView.as_view(),
         {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

]
