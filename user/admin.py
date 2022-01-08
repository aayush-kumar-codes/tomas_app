from django.contrib import admin
from .models import NewUser

class NewUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "city", "is_active")

admin.site.register(NewUser, NewUserAdmin)
