from django.db import models

class SubscriptionPackages(models.Model):
    id = models.BigAutoField(primary_key=True)
    length = models.BigIntegerField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subscription_packages'
