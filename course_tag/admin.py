from django.contrib import admin
from course_tag.models import CourseTags
from tag.models import Tags

class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'get_tag')

    @admin.display(description="tag")
    def get_tag(self, obj):
        tag = Tags.objects.filter(id=obj.tag_id).get()
        return tag.name

admin.site.register(CourseTags, CourseTagAdmin)