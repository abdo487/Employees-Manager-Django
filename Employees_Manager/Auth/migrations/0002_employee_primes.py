# Generated by Django 5.0.1 on 2024-01-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='primes',
            field=models.ManyToManyField(through='Auth.Prime', to='Auth.typeprime'),
        ),
    ]
