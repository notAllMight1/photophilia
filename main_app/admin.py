from django.contrib import admin
from .models import Photo, Comment, Like

# Register the Photo model
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_by', 'uploaded_at', 'caption')
    list_filter = ('uploaded_by', 'uploaded_at')
    search_fields = ('caption',)

# Register the Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'author', 'created_at', 'text')
    list_filter = ('author', 'created_at')
    search_fields = ('text',)

# Register the Like model
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'user', 'created_at')
    list_filter = ('user', 'created_at')
