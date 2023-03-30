from django.db import models

class Subscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('user.Users', models.DO_NOTHING, blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subscriptions'
