# Generated by Django 2.2.7 on 2019-11-11 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191111_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='questions',
            new_name='questions1',
        ),
    ]
