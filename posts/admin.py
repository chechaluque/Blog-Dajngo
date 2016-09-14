from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'update','timestamp']
    list_display_links = ['update']
    list_filter = ['update']
    search_fields = ['title', 'content']
    class Meta:
        model = Post
admin.site.register(Post, PostAdmin)

