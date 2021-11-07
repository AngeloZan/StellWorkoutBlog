from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, Profile

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'id', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'id')
    readonly_fields = ('date_joined', 'last_login', 'id')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Profile)
