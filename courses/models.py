from django.db import models
from membership.models import Membership
# Create your models here.

class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=20)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=300)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
