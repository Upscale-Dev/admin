from django.db import models
from category.models import Categories

# Create your models here.
class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
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

class Videos(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    thumbnail_url = models.TextField()
    main_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'videos'
