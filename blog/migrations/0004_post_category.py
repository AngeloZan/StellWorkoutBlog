# Generated by Django 3.1.3 on 2021-12-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211115_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('nenhuma', 'Nenhuma'), ('primeiros_passos', 'Primeiros Passos'), ('movimentos', 'Movimentos'), ('treinos', 'Treinos'), ('alimentacao', 'Alimentação'), ('descanso', 'Descanso')], default='nenhuma', max_length=25),
        ),
    ]
