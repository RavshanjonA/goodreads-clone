from django.contrib import admin

from book.models import Users, Book


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_filter = ("username",)
    list_display = ("first_name", "last_name", "middle_name", "username")
    list_display_links = ("username",)
    search_fields = ("username", "first_name")
    date_hierarchy = "date_joined"
