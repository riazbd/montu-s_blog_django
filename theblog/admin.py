from django.contrib import admin
from .models import Post, Comment, Category, Profile

# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
