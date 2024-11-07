from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from .models import Chat
from tickets.models import *
# Create your views here.


@login_required()
def chat(request, pk):

    user = request.user
    ticket = Tickets.objects.filter(pk=pk).first()
    chat_model = Chat.objects.filter(roomname=pk).first()

    if not chat_model.DoesNotExist():
        chat = Chat.objects.create(roomname=pk)
        chat.members.add(user)
    else:
        chat_model.members.add(user)

    username = request.user.username
    author = str(username)

    if username == str(ticket.expert):
        author = str(ticket.author)
    elif username == str(ticket.author):
        author = ticket.expert

    context = {
        'chat_name': ticket.name,
        'ticket': ticket,
        'author': author,
        'room_name': pk,
        'username': mark_safe(json.dumps(username))
    }

    return render(request, r"helpdesk\chat\templates\chat_app.html", context)
