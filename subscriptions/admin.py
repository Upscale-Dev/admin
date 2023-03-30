from django.contrib import admin
from subscriptions.models import Subscriptions

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'status', 'valid_until', 'created_at')

    @admin.display(description="user")
    def get_user(self, obj):
        return obj.user.fullname

admin.site.register(Subscriptions, SubscriptionAdmin)
