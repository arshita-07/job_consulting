# Generated by Django 3.1.4 on 2021-05-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='company_name',
            field=models.CharField(max_length=300),
        ),
    ]
