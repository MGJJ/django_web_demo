# Generated by Django 2.0.5 on 2018-10-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_recruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_de',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1, verbose_name='状态')),
                ('name', models.CharField(max_length=32)),
                ('salary', models.CharField(max_length=32, verbose_name='薪资')),
                ('company', models.CharField(max_length=32, verbose_name='就业单位')),
                ('img', models.ImageField(upload_to='./static/pic', verbose_name='头像')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1, verbose_name='状态')),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('summary', models.CharField(max_length=64, verbose_name='摘要')),
                ('detail', models.CharField(max_length=256, verbose_name='详细')),
            ],
            options={
                'verbose_name': '教师',
                'db_table': 'teacher',
            },
        ),
    ]
