from django.contrib import admin
# imports the model
from .models import djangoClasses

# registers the model
admin.site.register(djangoClasses)