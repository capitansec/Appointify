from django.db import migrations

def create_public_tenant(apps, schema_editor):
    Client = apps.get_model('tenants', 'Client')
    Domain = apps.get_model('tenants', 'Domain')

    # 🏢 Public Tenant oluştur
    client, created = Client.objects.get_or_create(
        schema_name='public',
        defaults={
            'name': 'Admin Paneli',
            'paid_until': '2099-12-31',
            'on_trial': False,
        }
    )
    client.auto_create_schema = False  # Public schema zaten var
    client.save()

    # 🌍 Public domain ekle
    Domain.objects.get_or_create(
        domain='admin.myappointments.com',  # Burayı kendi domaininize göre değiştirin
        tenant=client,
        defaults={'is_primary': True}
    )

class Migration(migrations.Migration):
    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_public_tenant)
    ]
