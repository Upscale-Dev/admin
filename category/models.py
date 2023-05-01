from django.db import models

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)

    class Meta:
        managed = True
        db_table = 'categories'