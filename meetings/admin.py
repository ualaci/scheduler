from django.contrib import admin
from .models import User, Meeting,Location

admin.site.register(User)
admin.site.register(Meeting)
admin.site.register(Location)