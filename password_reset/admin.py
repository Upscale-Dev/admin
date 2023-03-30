from django.contrib import admin
from password_reset.models import PasswordResets

class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('id', "get_user",'token', 'created_at', 'valid')

    @admin.display(description="user")
    def get_user(self, obj):
        return obj.user.fullname

admin.site.register(PasswordResets, PasswordResetAdmin)
