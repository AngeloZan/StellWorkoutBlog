from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_added', 'id')
    search_fields = ('title', 'intro', 'user__username', 'user__id', 'id')
    readonly_fields = ('date_added', 'user')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Post, PostAdmin)
