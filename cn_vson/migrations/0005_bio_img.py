# Generated by Django 2.1.3 on 2019-08-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_vson', '0004_auto_20190829_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio_category', models.CharField(max_length=100)),
                ('bio_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
