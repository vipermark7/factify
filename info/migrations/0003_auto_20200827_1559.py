# Generated by Django 3.0.8 on 2020-08-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20200827_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.CharField(default='', max_length=1000),
        ),
    ]