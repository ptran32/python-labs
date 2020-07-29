from django.contrib import admin

# Register your models here.

from .models import Topic, Entry # looks for module.py in the same directory as admin.py

# Say django to manage our model Topic through the admin site.
admin.site.register(Topic)
admin.site.register(Entry)
