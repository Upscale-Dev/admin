from django.db import models

class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tags'
