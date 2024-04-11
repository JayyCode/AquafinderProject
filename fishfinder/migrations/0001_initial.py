# Generated by Django 5.0.3 on 2024-03-21 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('USER_ID', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'aquafinder.users',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUSTOMER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfinder.users')),
            ],
            options={
                'db_table': 'aquafinder.transations',
            },
        ),
    ]
