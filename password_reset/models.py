from django.db import models

class PasswordResets(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('user.Users', models.DO_NOTHING, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    valid = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'
