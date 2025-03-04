"""
Django settings for myappointments project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-zgt(!zk)mwf*pi2q+$jmwu3__#w^gx$5!q^&r7)=*c-4%y-h8&'
DEBUG = True
ALLOWED_HOSTS = ['*']

# ✅ Tenant Tabanlı PostgreSQL Ayarları
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'myappointmentsdb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASE_ROUTERS = ['django_tenants.routers.TenantSyncRouter']

TENANT_MODEL = "tenants.Client"
TENANT_DOMAIN_MODEL = "tenants.Domain"

# ✅ Kullanıcı Yönetimi
AUTH_USER_MODEL = "tenants.TenantUser"
AUTHENTICATION_BACKENDS = [
    'tenants.auth_backends.TenantAuthBackend',  # Tenant bazlı auth
    'django.contrib.auth.backends.ModelBackend',  # Django default auth (admin için)
]
# ✅ Login / Logout Yönlendirmeleri
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

# ✅ SHARED_APPS: Ortak Uygulamalar
SHARED_APPS = (
    'django_tenants',  # Django Tenants en üste olmalı

    # Django Core Apps
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Tenant Yönetimi
    'tenants',
    'public',
)

# ✅ TENANT_APPS: Tenant'a Özel Uygulamalar
TENANT_APPS = (
    'appointments',
)

# ✅ INSTALLED_APPS: Django Tenants Gereksinimleri ile Düzenlendi
INSTALLED_APPS = [
    'jazzmin',  # Admin Paneli için Jazzmin UI
] + list(SHARED_APPS) + list(TENANT_APPS)

# ✅ Middleware Ayarları
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_tenants.middleware.main.TenantMainMiddleware',  # Django Tenants Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ URL ve WSGI Ayarları
ROOT_URLCONF = 'myappointments.urls'
WSGI_APPLICATION = 'myappointments.wsgi.application'

# ✅ Django Templates Konfigürasyonu
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ✅ Dil ve Zaman Ayarları
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static Dosya Ayarları
STATIC_URL = 'static/'

# ✅ Varsayılan Primary Key Ayarı
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Jazzmin Admin Paneli Konfigürasyonu
JAZZMIN_SETTINGS = {
    "site_title": "MyAppointments Admin",
    "site_header": "Booking Admin",
    "welcome_sign": "Hoş Geldiniz",
    # Daha fazla Jazzmin ayarı buraya eklenebilir.
}
