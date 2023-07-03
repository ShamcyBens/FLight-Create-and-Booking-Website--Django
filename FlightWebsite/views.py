from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm, FlightCreateForm
from django.contrib.auth.decorators import login_required
from .models import Flight
from django.contrib import messages


# Create your views here.
def home(request):    
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def create_flight(request):
    if request.method == 'POST':
        form = FlightCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight created successfully and added to the flight list.')
            return redirect('flight-list')
    else:
        form = FlightCreateForm()
    return render(request, 'create_flight.html', {'form': form})


def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

def flight_detail(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, 'flight_detail.html', {'flight': flight})

def flight_update(request, pk):
    flight = Flight.objects.get(pk=pk)
    if request.method == 'POST':
        form = FlightCreateForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlightCreateForm(instance=flight)
    return render(request, 'flight_update.html', {'form': form})