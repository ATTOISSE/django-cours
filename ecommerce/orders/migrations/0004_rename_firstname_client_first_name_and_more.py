# Generated by Django 5.0.6 on 2024-06-24 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_client_age_client_lastname_alter_client_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
