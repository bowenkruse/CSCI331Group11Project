# Generated by Django 3.2.5 on 2021-10-28 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('Profile', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='courses',
            field=models.ManyToManyField(to='course.course_model'),
        ),
    ]
