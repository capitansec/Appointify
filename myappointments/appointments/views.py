from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def dashboard(request):
    user_appointments = Appointment.objects.filter(owner=request.user)
    return render(request, 'appointments/dashboard.html', {"appointments": user_appointments})
