# Generated by Django 3.1.4 on 2021-07-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210706_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='image',
            field=models.ImageField(default='default.PNG', upload_to='media'),
        ),
    ]
