from django.contrib import admin
from subscription_package.models import SubscriptionPackages

class SubscriptionPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'price', 'description')

admin.site.register(SubscriptionPackages, SubscriptionPackageAdmin)