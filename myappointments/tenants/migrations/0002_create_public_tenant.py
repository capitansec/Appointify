from django.db import migrations

def create_public_tenant(apps, schema_editor):
    Client = apps.get_model('tenants', 'Client')
    Domain = apps.get_model('tenants', 'Domain')

    client, created = Client.objects.get_or_create(
        schema_name='public',
        defaults={
            'name': 'Public Tenant'
            # 'auto_create_schema': False => HATALI, bu DB alanı değil
        }
    )
    # Burada Python seviyesinde ayarlayabilirsiniz:
    client.auto_create_schema = False
    client.save()

    Domain.objects.get_or_create(
        domain='127.0.0.1',
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
