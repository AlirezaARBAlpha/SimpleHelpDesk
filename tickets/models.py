from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
from users.models import User


class Tickets(models.Model):
    expert = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='expert', db_column='expert',)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author', db_column='username',)

    name = models.CharField(max_length=200)
    description = models.TextField()
    STATUS_CHOICES = (
        ('Open', 'open'),
        ('Pending', 'pending'),
        ('Closed', 'closed')
    )

    SET_PRIORITY = (
        ('critical', 'Critical'),
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
        ('not_important', 'Not Important'),
    )

    SET_CATEGORY = (
        ('problem', 'Problem'),
        ('question', 'Question'),
        ('request_development', 'Request Development'),
        ('event', 'Event'),
    )

    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='Open')
    priority = models.CharField(
        max_length=100, choices=SET_PRIORITY, default='not_important')
    category = models.CharField(
        max_length=100, choices=SET_CATEGORY, default='problem')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat:chat_page', args=[str(self.pk)])
