from django.contrib import admin

# Register your models here.
from .models import UserProfile, Experience, Education, Certification

admin.site.register(UserProfile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certification)
