# Generated by Django 5.0.6 on 2024-06-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_client_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='lastName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='firstName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
