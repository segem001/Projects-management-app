from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    avatar = models.ImageField(upload_to='photos/',null=True)
    fullname = models.CharField(max_length=255,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = HTMLField(null=True)
    email = models.EmailField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()

    def __str__(self):
        return self.username.username

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(username__username=search_term) | Q(fullname__icontains=search_term))
        return profiles



class Project(models.Model):
    title = models.CharField(max_length=200,)
    uploaded_by = models.ForeignKey(Profile, related_name='poster')
    landing_image = models.ImageField(upload_to='photos/',)
    screen_one = models.ImageField(upload_to='photos/', blank=True)
    screen_two = models.ImageField(upload_to='photos/', blank=True)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200,)
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def all_projects(cls):
        all_projects = cls.objects.all()
        return all_projects

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(Q(description__icontains=search_term) | Q(title__icontains=search_term))

    def get_user_projects(self, post):
        projects = self.objects.filter(uploaded_by=post.uploaded_by)
        return projects

    def get_one_project(self, post_id):
        return self.objects.get(pk=post_id)

    def save_post(self, user):
        self.uploaded_by = user
        self.save()

    def get_last_project(cls):
        return cls.objects.last()

    def __str__(self):
        return self.title



class Rating(models.Model):
    user = models.ForeignKey(Profile, related_name='ratings', null=True)
    project = models.ForeignKey(Project, related_name='ratings', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    usability = models.IntegerField(default=0,)
    design = models.IntegerField(default=0,)
    content = models.IntegerField(default=0,)
    creativity = models.IntegerField(default=0,)
    score = models.IntegerField(default=0,)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.user} + {self.project}"
