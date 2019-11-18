# Generated by Django 2.2.7 on 2019-11-11 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191108_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='answer1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Question'),
        ),
    ]
