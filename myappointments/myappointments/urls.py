# myappointments/myappointments/urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from public.views import home
from appointments.views import dashboard, create_appointment

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Login/Logout (tenant bazında da çalışacak)
    path('login/', auth_views.LoginView.as_view(template_name='appointments/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),

    # Tenant kullanıcıları için randevu işlemleri
    path('dashboard/', dashboard, name='dashboard'),
    path('appointments/create/', create_appointment, name='create_appointment'),

    # Public ana sayfa
    path('', home, name='home'),
]
