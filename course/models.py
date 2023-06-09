from django.db import models


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    description = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'categories'

    def __str__(self) -> str:
        return f"[{self.id}] {self.name}"


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tags'


class CourseTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField(blank=True, null=True)
    tag_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'course_tags'


class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(
        Categories, models.CASCADE, blank=True, null=True)
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

    def __str__(self) -> str:
        return f"[{self.id}] {self.name}"


STATUS_CHOICES = [
    ('ON PROGRESS', 'ON PROGRESS'),
    ('COMPLETED', 'COMPLETED'),
]


class CourseProgress(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    course_id = models.BigIntegerField(blank=True, null=True)
    videos_watched = models.BigIntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, choices=STATUS_CHOICES)

    class Meta:
        managed = True
        db_table = 'course_users'


class Videos(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.ForeignKey(
        Courses, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    thumbnail_url = models.TextField()
    main_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'videos'

    def __str__(self) -> str:
        return f"[{self.id}] {self.name}"
