from django.contrib import admin
from user.models import Users, PasswordResets

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'fullname', 'created_at', 'type', 'subscription_until')
    
admin.site.register(Users, UserAdmin)

class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('id', "get_user",'token', 'created_at', 'valid')

    @admin.display(description="user")
    def get_user(self, obj):
        return obj.user.fullname

admin.site.register(PasswordResets, PasswordResetAdmin)