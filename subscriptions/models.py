from django.db import models

STATUS_CHOICES = [
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Invalid', 'Invalid')
]
class Subscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('user.Users', models.CASCADE, blank=True, null=True)
    status = models.TextField(blank=True, null=True, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    package_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subscriptions'

class SubscriptionPackages(models.Model):
    id = models.BigAutoField(primary_key=True)
    length = models.BigIntegerField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subscription_packages'