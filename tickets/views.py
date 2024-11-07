from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import *
from users.models import *
from setting.models import UserRole
from chat.models import *
# from django.contrib.auth.models import User
# Create your views here.


@login_required()
def create_ticket(request):
    if request.method == 'POST':

        user = User.objects.get(username=request.POST['expert'])
        chatroom = Chat()
        ticket = Tickets()
        ticket.author = request.user
        ticket.category = request.POST['category']
        ticket.name = request.POST['name']
        ticket.expert = user
        ticket.priority = request.POST['priority']
        ticket.description = request.POST['description']
        ticket.save()

        chatroom.roomname = ticket.pk
        chatroom.ticket = ticket
        chatroom.save()

        return redirect('/account')

    else:
        experts = UserRole.objects.filter(
            role__name__contains='expert')

        context = {
            'experts': experts
        }
        return render(request, r'helpdesk\tickets\templates\index.html', context)
