# Generated by Django 2.1.3 on 2019-09-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_vson', '0002_auto_20190905_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(null=True),
        ),
    ]