# tenants/admin.py
from django.contrib import admin
from django import forms   # <-- YENİ
from .models import Client, Domain

# 1) Özel Form
class ClientForm(forms.ModelForm):
    """
    Bu form, Client oluştururken ek olarak 'domain' alanı girmemize izin verir.
    Domain girmeseniz de kaydı tamamlayabilirsiniz.
    """
    domain = forms.CharField(
        required=False,
        label="Domain (isteğe bağlı)",
        help_text="Bu tenant'a ait domain/subdomain (örn: tenant1.domain.com)",
    )

    class Meta:
        model = Client
        fields = ['schema_name', 'name', 'paid_until', 'on_trial']
        # NOT: 'domain' modeli bir alan olmadığı için, Meta.fields'e eklenmez.

# 2) Admin sınıfı
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm  # <-- YENİ: Admin’de kullanacağımız form

    list_display = ('name', 'schema_name')

    def save_model(self, request, obj, form, change):
        """
        Client kaydedilirken eğer 'domain' alanı doldurulduysa
        otomatik olarak Domain modeli oluştur.
        """
        super().save_model(request, obj, form, change)  # Önce Client kaydı

        domain_value = form.cleaned_data.get('domain')  # Form'daki domain
        if domain_value:
            # Domain zaten varsa oluşmasın, yoksa yaratalım:
            Domain.objects.get_or_create(
                domain=domain_value,
                tenant=obj,
                defaults={'is_primary': True}
            )

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
