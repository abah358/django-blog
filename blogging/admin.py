from django.contrib import admin

from blogging.models import Post, Category, CategoryInline, PostAdmin

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
