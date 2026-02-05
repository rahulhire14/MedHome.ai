from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'full_name',
        'gender',
        'PhoneNumber',
        'created_on',
    )

    search_fields = (
        'full_name',
        'user__username',
        'PhoneNumber',
    )

    list_filter = ('gender', 'created_on')

    fieldsets = (
        ("User Info", {
            "fields": ('user', 'full_name', 'gender')
        }),
        ("Contact Details", {
            "fields": ('phone_number', 'address')
        }),
        ("Timestamps", {
            "fields": ('created_on', 'updated_on')
        }),
    )

    readonly_fields = ('created_on', 'updated_on')
