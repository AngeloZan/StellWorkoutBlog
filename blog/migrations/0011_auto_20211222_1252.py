# Generated by Django 3.1.3 on 2021-12-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20211222_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='readable_name',
            field=models.CharField(default='', max_length=25, verbose_name='Nome legível'),
            preserve_default=False,
        ),
    ]