from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.hashers import make_password


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)

    auto_create_schema = True  # Yeni tenant oluşunca otomatik schema oluşturulsun

    def save(self, *args, **kwargs):
        # Yeni tenant oluşturuluyorsa önce kaydet
        is_new = self._state.adding  # Yeni oluşturuluyor mu?
        super().save(*args, **kwargs)

        if is_new:
            # 🌟 Yeni tenant oluşturulunca bir user da ekleyelim
            from tenants.models import TenantUser
            admin_user = TenantUser.objects.create(
                username=f"admin_{self.schema_name}",
                email=f"admin@{self.schema_name}.com",
                password=make_password("Admin123"),  # Default şifre
                tenant=self
            )
            admin_user.is_staff = True
            admin_user.is_superuser = False  # Müşteri admin, ama superuser değil
            admin_user.save()

class Domain(DomainMixin):
    """Subdomain veya domain bazlı yönlendirme için model"""
    pass


class TenantUser(AbstractUser):
    """
    Tenant bazlı kullanıcı modeli.
    Her tenant kendi kullanıcılarını yönetir.
    """
    email = models.EmailField(unique=True)
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return f"{self.username} ({self.tenant.name})"
