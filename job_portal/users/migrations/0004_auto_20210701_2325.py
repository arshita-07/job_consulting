# Generated by Django 3.1.4 on 2021-07-01 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_newsletter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsLetter',
            new_name='NewsLetterModel',
        ),
    ]
