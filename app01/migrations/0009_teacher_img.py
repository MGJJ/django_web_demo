# Generated by Django 2.0.5 on 2018-10-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20181001_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='img',
            field=models.ImageField(default='', upload_to='./static/pic', verbose_name='头像'),
        ),
    ]
