from django.contrib import admin
from course.models import Courses, Videos

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'name', 'description', 'image_url', 'trailer_url', 'created_at', 'updated_at', 'deleted_at')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'name', 'description', 'thumbnail_url', 'main_url')

admin.site.register(Courses, CourseAdmin)
admin.site.register(Videos, VideoAdmin)
