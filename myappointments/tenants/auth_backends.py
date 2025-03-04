from django.contrib.auth.backends import ModelBackend
from tenants.models import TenantUser

class TenantAuthBackend(ModelBackend):
    """
    Tenant bazlı kimlik doğrulama backend'i.
    Superuser'ların normal tenant login yapmasını engeller.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = TenantUser.objects.get(username=username)
            if user.check_password(password):
                # ❌ Superuser ise girişe izin verme
                if user.is_superuser:
                    return None
                return user
        except TenantUser.DoesNotExist:
            return None
        return None
