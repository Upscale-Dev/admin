from django.db import models

# Create your models here.
class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField()
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    trailer_url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'