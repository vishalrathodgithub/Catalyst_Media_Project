from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title','post_details','post_created']

admin.site.register(Post,PostAdmin)