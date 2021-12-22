from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_added', 'id')
    search_fields = ('title', 'intro', 'categories', 'user__username', 'user__id', 'id')
    readonly_fields = ('date_added', 'user')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'readable_name', 'id')
    search_fields = ('name', 'readable_name', 'id')
    readonly_fields = ('date_added',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)