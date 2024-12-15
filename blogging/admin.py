from django.contrib import admin
from blogging.models import Post, Category


# Define an inline admin descriptor for Category (linked to Post)
class CategoryInline(admin.TabularInline):
    model = Post.categories.through  # Many-to-Many intermediate table
    extra = 1  # Number of empty forms displayed in the inline admin


# Customize the Post admin view
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    list_filter = ('author', 'created_date', 'published_date')


# Customize the Category admin view
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)  # Exclude the reverse Many-to-Many field


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
