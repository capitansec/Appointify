# appointments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm

@login_required
def dashboard(request):
    # Giriş yapmış kullanıcının randevularını listeleyelim
    apps = Appointment.objects.filter(owner=request.user)
    return render(request, 'appointments/dashboard.html', {"apps": apps})

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.owner = request.user
            appointment.save()
            return redirect('dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create_appointment.html', {'form': form})
