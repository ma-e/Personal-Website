# Generated by Django 2.1.3 on 2019-09-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_vson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
