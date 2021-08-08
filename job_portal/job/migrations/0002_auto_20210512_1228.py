# Generated by Django 3.1.4 on 2021-05-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(related_name='applicants', through='job.Application', to='users.WorkingUser'),
        ),
        migrations.AlterField(
            model_name='job',
            name='apply_deadline',
            field=models.DateTimeField(null=True, verbose_name='Apply by'),
        ),
    ]