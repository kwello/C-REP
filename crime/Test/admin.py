from django.contrib import admin
from test.models import AuthUsers

# Register your models here.
class AuthUsersAdmin(admin.ModelAdmin):
    model = AuthUsers

    list_display = ["emailid", "fname", "lname", "address"]
    list_filter = ["emailid"]

admin.site.site_title = "Employee Database"
admin.site.site_header = "Employee Management System"

admin.site.register(AuthUsers, AuthUsersAdmin)