from django.contrib import admin
from subscriptions.models import Subscriptions, SubscriptionPackages
from dateutil.relativedelta import relativedelta
from user.models import Users
from subscriptions.models import Subscriptions
from datetime import datetime
import pytz

class SubscriptionAdmin(admin.ModelAdmin):
    actions = ['make_active']
    list_display = ('id', 'get_user', 'status', 'package_id', 'created_at')

    @admin.action(description="Mark select subscription as active")
    def make_active(self, request, queryset):
        for q in queryset:
            if q.status == 'Active':
                continue
            
            user = Users.objects.filter(id=q.user.id).get()
            package = SubscriptionPackages.objects.filter(id=q.package_id).get()
            existing_subscribption = Subscriptions.objects.filter(user=user.id, status='Active').exclude(id=q.id).first()
            
            if (existing_subscribption is None):
                user.subscription_until = datetime.now(pytz.timezone('Asia/Jakarta'))

            user.subscription_until = user.subscription_until + relativedelta(months=package.length)
            user.save()

            q.status = 'Active'
            q.save()

    @admin.display(description="user")
    def get_user(self, obj):
        return obj.user.fullname

admin.site.register(Subscriptions, SubscriptionAdmin)

class SubscriptionPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'price', 'description')

admin.site.register(SubscriptionPackages, SubscriptionPackageAdmin)
