from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    list_filter = ('author', 'created_date', 'published_date')


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
