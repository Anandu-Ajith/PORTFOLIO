from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


#class Portfolio(models.Model):
   # name = models.CharField(max_length=20)

   # contact = models.CharField(max_length=200)
 #   skills = models.CharField(max_length=250)
   # password = models.CharField(max_length=50)
   # confirmpassword = models.CharField(max_length=50)

  #  def __str__(self):
   #     return self.name

class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        contact = models.CharField(max_length=200, default='contact address')
        skills = models.TextField(max_length=255, blank=True)
        contact_email = models.EmailField(max_length=20, blank=True)
        profile_picture = models.ImageField(upload_to='profile_pics', default='default.jpg')

        def __str__(self):
            return f'{self.user.username} Profile'

        def get_absolute_url(self):
            return reverse('profile', kwargs={'pk': self.pk})


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=560)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Make sure Portfolio is imported or defined in your models.py
    portfolio = models.ForeignKey('UserProfile', on_delete=models.CASCADE,null=True, blank=True)  # ForeignKey to Portfolio model

    def __str__(self):
        return self.title



class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.position} at {self.company}'

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.degree} in {self.field_of_study}'

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.name



