from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=75, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class group(models.Model):
    group_name = models.CharField(max_length=75, blank=False)
    course_in = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.group_name
