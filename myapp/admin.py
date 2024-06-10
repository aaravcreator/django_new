from django.contrib import admin

# Register your models here.
from .models import Person,Mission

admin.site.register([Person,Mission])