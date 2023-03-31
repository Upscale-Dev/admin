from django.db import models

TYPE_CHOICES = [
    ('Google', 'Google'),
    ('Credential', 'Credential'),
]

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.TextField(unique=True)
    fullname = models.TextField(blank=True, null=True)
    hashed_password = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True, choices=TYPE_CHOICES)
    subscription_until = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'

