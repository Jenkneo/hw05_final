# Generated by Django 2.2.9 on 2022-09-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220915_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
