# Generated by Django 5.2 on 2025-05-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
