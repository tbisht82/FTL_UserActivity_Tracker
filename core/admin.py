from django.contrib import admin
from .models import User, ActivityPeriod

# Register User and ActivityPeriod models to admin panel
admin.site.register(User)
admin.site.register(ActivityPeriod)
