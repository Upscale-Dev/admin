from django.contrib import admin
from course.models import Courses

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'name', 'description', 'image_url', 'trailer_url', 'created_at', 'updated_at', 'deleted_at')

admin.site.register(Courses, CourseAdmin)
