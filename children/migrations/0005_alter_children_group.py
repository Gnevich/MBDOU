# Generated by Django 4.2 on 2023-05-21 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0004_alter_childrengroup_groupage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='Group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='children.childrengroup', verbose_name='Группа'),
        ),
    ]
