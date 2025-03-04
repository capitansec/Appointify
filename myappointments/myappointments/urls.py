# myappointments/myappointments/urls.py

from django.contrib import admin
from django.urls import path
from public.views import home  # Dikkat: from public.views import ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Boş path => anasayfa
]
