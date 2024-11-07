from django.urls import path

from . import views

urlpatterns = [
    path('', views.user, name='user_account'),
    path('ExpertAccount/', views.expert, name='expert_account'),
]
