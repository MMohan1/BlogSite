from django.contrib import admin
from blogs.models import Blog, Action


class ActionInline(admin.StackedInline):  # StackedInline for line by line
    model = Action
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Blog Details', {'fields': [('Blog_Title', 'Blog_Field')]}),
        ('Blog Description', {'fields': ['URL', 'Blog_Description']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ('Block Like', {'fields': ['Like']}),
    ]
    inlines = [ActionInline]
    list_display = ('Blog_Title', 'Blog_Field', 'URL', 'Like')
    list_filter = ['Blog_Field']
    search_fields = ['Blog_Title']
admin.site.register(Blog, BlogAdmin)
