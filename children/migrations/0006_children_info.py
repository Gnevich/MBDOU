# Generated by Django 4.2 on 2023-05-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0005_alter_children_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='children',
            name='Info',
            field=models.CharField(default='', max_length=200, verbose_name='Информация'),
        ),
    ]