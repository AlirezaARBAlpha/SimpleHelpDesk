from django.contrib import admin
from .models import Tickets


@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ['author', 'expert', 'name',
                    'status', 'priority', 'updated', 'created']
