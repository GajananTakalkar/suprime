# Generated by Django 4.0.5 on 2022-08-18 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('git', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='addr',
            new_name='Addr',
        ),
    ]
