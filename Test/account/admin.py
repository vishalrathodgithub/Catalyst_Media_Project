from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Password','Date_Of_Birth','Mobile_Number']

admin.site.register(User,UserAdmin)