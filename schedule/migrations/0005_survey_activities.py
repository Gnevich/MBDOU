# Generated by Django 4.2 on 2023-05-22 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_survey_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='Activities',
            field=models.CharField(choices=[('Социально-комуникативное развитие', 'Социально-комуникативное развитие'), ('Познавательное развитие', 'Познавательное развитие'), ('Речевое развитие', 'Речевое развитие'), ('Художественно-эстетическое развитие', 'Художественно-эстетическое развитие'), ('Физическое развитие', 'Физическое развитие')], default='Социально-комуникативное развитие', max_length=50),
        ),
    ]