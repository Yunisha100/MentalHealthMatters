# Generated by Django 4.1.4 on 2022-12-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_student_class_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'Admin'), (2, 'Teacher'), (3, 'Student')], default=3, max_length=50),
        ),
    ]
