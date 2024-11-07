from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from setting.models import *
from tickets.models import *
# Create your views here.


@login_required
def user(request):
    tickets = Tickets.objects.filter(author=request.user)
    open_tickets = tickets.filter(status='Open')
    context = {
        'tickets': open_tickets
    }
    return render(request, r'D:\Project Test\Django 2\helpdesk\account\templates\user.html', context)


@login_required
def expert(request):
    tickets = Tickets.objects.filter(expert=request.user)
    open_tickets = tickets.filter(status='Open')
    finished_tickets = tickets.filter(
        status='Closed')

    context = {
        'open_tickets': open_tickets,
        'finished_tickets': finished_tickets,
    }
    return render(request, r'D:\Project Test\Django 2\helpdesk\account\templates\expert.html', context)
