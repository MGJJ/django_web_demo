# Generated by Django 2.0.5 on 2018-09-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bxslider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('href', models.CharField(max_length=256, verbose_name='跳转地址')),
                ('img', models.ImageField(upload_to='./static/imag', verbose_name='图片')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '轮播图',
                'db_table': 'bxsilder',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1, verbose_name='状态')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('icon', models.ImageField(upload_to='./static/icon', verbose_name='图标')),
                ('summary', models.CharField(max_length=32, verbose_name='摘要')),
            ],
            options={
                'verbose_name': '课程',
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1, verbose_name='状态')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('detail', models.TextField(verbose_name='详情')),
            ],
            options={
                'verbose_name': '公告',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1, verbose_name='状态')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='姓名')),
                ('img', models.ImageField(upload_to='./static/pic', verbose_name='头像')),
                ('company', models.CharField(max_length=32, verbose_name='就业单位')),
                ('detail', models.TextField(verbose_name='详细信息')),
                ('salary', models.CharField(max_length=32, verbose_name='薪资')),
            ],
            options={
                'verbose_name': '学生',
                'db_table': 'student',
            },
        ),
    ]
