from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.chat, name="chat_page"),
    # path("", views.chat, name="chat-page"),

]
