# Generated by Django 2.2.4 on 2021-11-29 21:33

from django.db import migrations

def transfer_data(apps, shema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner_flats = Flat.objects.filter(
            owner=owner.owner,
            owners_phonenumber_formatted=owner.owners_phonenumber_formatted
        )
        for flat in owner_flats:
            owner.flats_in_property.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20211129_0251'),
    ]

    operations = [
        migrations.RunPython(transfer_data)
    ]