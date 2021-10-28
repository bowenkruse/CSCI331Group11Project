from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from course.models import Course


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images', null=True, blank=True)
    gpa = models.FloatField(default=4.0)
    rating = models.FloatField(default=5.0, editable=False)
    slug = AutoSlugField(populate_from='user')
    bio = models.CharField(max_length=255, blank=True, help_text="Tell us something about you")
    courses = models.ManyToManyField(Course)
    # todo put relationship with course app in here?

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return "/Profile/{}".format(self.slug)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
