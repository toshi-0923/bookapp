# Generated by Django 3.0.2 on 2020-01-28 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aggregate',
            old_name='colomun',
            new_name='columun',
        ),
        migrations.RenameField(
            model_name='aggregate',
            old_name='colomun_type',
            new_name='columun_type',
        ),
    ]
