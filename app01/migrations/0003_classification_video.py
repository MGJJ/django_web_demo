# Generated by Django 2.0.5 on 2018-09-25 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180925_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
            ],
            options={
                'verbose_name': '等级',
                'db_table': 'classification',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1, verbose_name='状态')),
                ('level', models.IntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], default=1, verbose_name='等级')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('href', models.CharField(max_length=256, verbose_name='播放地址')),
                ('img', models.ImageField(upload_to='.static/icon', verbose_name='封面')),
                ('summary', models.CharField(max_length=32, verbose_name='摘要')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Classification')),
            ],
            options={
                'verbose_name': '视频',
                'db_table': 'video',
            },
        ),
    ]
