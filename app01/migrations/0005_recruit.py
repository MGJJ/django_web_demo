# Generated by Django 2.0.5 on 2018-10-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20180925_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=1, verbose_name='状态')),
                ('name', models.CharField(max_length=32, verbose_name='题目')),
                ('salary', models.CharField(max_length=64, verbose_name='薪酬')),
            ],
            options={
                'verbose_name': '招聘信息',
                'db_table': 'recruit',
            },
        ),
    ]