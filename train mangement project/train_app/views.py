from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Train

def train_list(request):
    trains = Train.objects.all()
    return render(request, 'train_list.html', {'trains': trains})

def add_train(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        departure_time = request.POST.get('departure_time')
        arrival_time = request.POST.get('arrival_time')
        seats_available = request.POST.get('seats_available')
        ticket_price = request.POST.get('ticket_price')
        
        Train.objects.create(
            name=name,
            number=number,
            source=source,
            destination=destination,
            departure_time=departure_time,
            arrival_time=arrival_time,
            seats_available=seats_available,
            ticket_price=ticket_price
        )
        messages.success(request, 'Train added successfully!')
        return redirect('train_list')
    
    return render(request, 'add_train.html')