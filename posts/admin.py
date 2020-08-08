from django.contrib import admin

# Register your models here.
from.models import Author, Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "thumbnail", 'author', 'timestamp',)
    list_filter = ('featured',)
    search_fields = ['title', 'content']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', "profile_picture",)
    search_fields = ['user']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)