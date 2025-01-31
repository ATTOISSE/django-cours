# Generated by Django 5.0.6 on 2024-07-01 20:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('command_number', models.UUIDField(default=uuid.uuid4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commands', to='orders.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
