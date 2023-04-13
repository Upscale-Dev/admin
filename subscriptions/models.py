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
    length = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    package_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subscriptions'
