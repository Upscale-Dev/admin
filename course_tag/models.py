from django.db import models

class CourseTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField(blank=True, null=True)
    tag_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'course_tags'
