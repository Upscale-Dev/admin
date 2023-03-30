from django.contrib import admin
from password_reset.models import PasswordResets

class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'created_at', 'valid')

admin.site.register(PasswordResets, PasswordResetAdmin)
