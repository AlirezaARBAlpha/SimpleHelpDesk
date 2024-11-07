from django.db import models
from users.models import User
from tickets.models import *


class Chat(models.Model):
    roomname = models.CharField(blank=True, max_length=50)
    members = models.ManyToManyField(User, null=True, blank=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)

    def __str__(self):
        return self.roomname


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # receiver = models.ManyToManyField(user, null=True, blank=True)
    content = models.TextField()
    related_chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def last_message(self, roomname):
        return Message.objects.filter(related_chat__roomname=roomname)

    def __str__(self):
        return self.author.username
