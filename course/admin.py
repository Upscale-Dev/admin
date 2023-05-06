from django.contrib import admin
from course.models import Courses

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_category', 'description', 'image_url', 'trailer_url', 'files')

    @admin.display(description="category")
    def get_category(self, obj):
        return obj.category.name
    
admin.site.register(Courses, CourseAdmin)