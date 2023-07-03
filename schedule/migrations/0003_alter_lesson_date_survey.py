# Generated by Django 4.2 on 2023-05-22 00:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0005_alter_children_group'),
        ('schedule', '0002_alter_lesson_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 5, 22), null=True, verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateField(default=datetime.date(2023, 5, 22), null=True, verbose_name='Год')),
                ('Season', models.CharField(choices=[('Сентябрь', 'Сентябрь'), ('Май', 'Май')], default='Сентябрь', max_length=9)),
                ('Group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='children.childrengroup', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Опросник',
                'verbose_name_plural': 'Опросник',
                'ordering': ('Year', 'Season'),
            },
        ),
    ]
