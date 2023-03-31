from django.contrib import admin
from user.models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'fullname', 'created_at', 'type', 'subscription_until')
    
admin.site.register(Users, UserAdmin)