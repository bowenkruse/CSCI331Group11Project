# Generated by Django 3.2.5 on 2021-10-28 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_userprofile_courses'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course_model',
            new_name='Courses',
        ),
    ]