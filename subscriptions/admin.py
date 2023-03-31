from django.contrib import admin
from subscriptions.models import Subscriptions
from dateutil.relativedelta import relativedelta
from user.models import Users
from subscriptions.models import Subscriptions
from datetime import datetime
import pytz

class SubscriptionAdmin(admin.ModelAdmin):
    actions = ['make_active']
    list_display = ('id', 'get_user', 'status', 'length', 'created_at')

    @admin.action(description="Mark select subscription as active")
    def make_active(self, request, queryset):
        for q in queryset:
            if q.status == 'Active':
                continue
            Subscriptions.objects.filter(id=q.id).update(status='Active')
            user = Users.objects.filter(id=q.user.id).get()
            if (user.subscription_until.strftime("%Y") == "0001"):
                user.subscription_until = datetime.now(pytz.timezone('Asia/Jakarta'))
            user.subscription_until = user.subscription_until + relativedelta(months=q.length)
            user.save()

    @admin.display(description="user")
    def get_user(self, obj):
        return obj.user.fullname

admin.site.register(Subscriptions, SubscriptionAdmin)
