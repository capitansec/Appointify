# tenants/models.py
from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)

    auto_create_schema = True  # Yeni tenant oluşturulunca otomatik şema
    # auto_drop_schema = True  # Tenant silinince şemayı düşürmek isterseniz

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    """
    Subdomain veya domain bazlı yönlendirme (client1.domain.com vb.)
    """
    pass
