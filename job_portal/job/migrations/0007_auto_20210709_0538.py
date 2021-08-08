# Generated by Django 3.1.4 on 2021-07-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20210525_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='work from home only', max_length=300),
        ),
        migrations.AddField(
            model_name='job',
            name='work_from_home',
            field=models.BooleanField(default=False),
        ),
    ]