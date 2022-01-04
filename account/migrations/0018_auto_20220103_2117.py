# Generated by Django 3.1.3 on 2022-01-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_account_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.AddField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='nascimento'),
        ),
    ]
