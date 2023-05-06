from django.db import models
from category.models import Categories

class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Categories, models.CASCADE, blank=True, null=True)
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    trailer_url = models.TextField()
    files = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'courses'
