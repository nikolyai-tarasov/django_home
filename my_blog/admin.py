from django.contrib import admin
from my_blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "heading", "description", "created_at",)
    list_filter = ("created_at", "views_counter",)
    search_fields = ("heading", "created_at",)