from django.contrib import admin
from course_tag.models import CourseTags
from course.models import Courses
from tag.models import Tags

class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_course', 'get_tag')

    @admin.display(description="course")
    def get_course(self, obj):
        course = Courses.objects.filter(id=obj.course_id).get()
        return course.name

    @admin.display(description="tag")
    def get_tag(self, obj):
        tag = Tags.objects.filter(id=obj.tag_id).get()
        return tag.name

admin.site.register(CourseTags, CourseTagAdmin)