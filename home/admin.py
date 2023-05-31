from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', 'get_image')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{obj.image.url}" width="100px" height=100px />')
        else:
            return 'Not Image'