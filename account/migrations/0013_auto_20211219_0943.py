# Generated by Django 3.1.3 on 2021-12-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_account_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Já existe uma conta com este email.'}, max_length=60, unique=True),
        ),
    ]
