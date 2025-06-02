from django.contrib import admin
from .models import Train

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'source', 'destination', 'departure_time', 'arrival_time', 'seats_available', 'ticket_price')
    search_fields = ('name', 'number', 'source', 'destination')
    list_filter = ('source', 'destination')