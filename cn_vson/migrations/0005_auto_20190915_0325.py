# Generated by Django 2.1.3 on 2019-09-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_vson', '0004_auto_20190915_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
