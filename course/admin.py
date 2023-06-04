from django.contrib import admin
from course.models import Courses, Categories, Tags, CourseTags, CourseProgress, Videos
from user.models import Users
from course.forms import CourseAdminForm, VideoAdminForm


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_category', 'description',
                    'image_url', 'trailer_url', 'files', 'created_at')

    @admin.display(description="category")
    def get_category(self, obj):
        return obj.category.name

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            self.form = CourseAdminForm

        return super().get_form(request, obj, **kwargs)


admin.site.register(Courses, CourseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Categories, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Tags, TagAdmin)


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


class CourseProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'get_course', 'videos_watched', 'status')

    @admin.display(description="user")
    def get_user(self, obj):
        user = Users.objects.filter(id=obj.user_id).get()
        return user.fullname

    @admin.display(description="course")
    def get_course(self, obj):
        course = Courses.objects.filter(id=obj.course_id).get()
        return course.name


admin.site.register(CourseProgress, CourseProgressAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_course', 'name', 'description',
                    'thumbnail_url', 'main_url')

    @admin.display(description="course")
    def get_course(self, obj):
        return obj.course.name

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            self.form = VideoAdminForm
        return super().get_form(request, obj, **kwargs)


admin.site.register(Videos, VideoAdmin)
