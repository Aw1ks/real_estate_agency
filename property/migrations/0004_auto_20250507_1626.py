# Generated by Django 5.2 on 2025-05-07 13:26

from django.db import migrations


def filtering_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year < 2015:
            flat.new_building = False
        else:
            flat.new_building = True
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_flat_has_balcony_alter_flat_id'),
    ]

    operations = [
        migrations.RunPython(filtering_buildings),
    ]
