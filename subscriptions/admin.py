from django.contrib import admin
from subscriptions.models import Subscriptions

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'valid_until', 'created_at')

admin.site.register(Subscriptions, SubscriptionAdmin)
