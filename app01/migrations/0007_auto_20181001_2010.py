# Generated by Django 2.0.5 on 2018-10-01 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_student_de_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student_de',
            options={'verbose_name': '学生'},
        ),
        migrations.AlterModelTable(
            name='student_de',
            table='student_de',
        ),
    ]