# Generated by Django 2.2.9 on 2022-09-14 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220914_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='address',
            new_name='slug',
        ),
    ]