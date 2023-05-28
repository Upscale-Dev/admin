from typing import Any
from django import forms

from course import utils
from course.models import Courses

class CourseAdminForm(forms.ModelForm):
    thumbnail_image = forms.FileField(label="Thumbnail Image", required=True)
    trailer_video = forms.FileField(label="Trailer Video", required=True)

    def save(self, commit=True) -> Any:
        thumbnail_image = self.cleaned_data.get('thumbnail_image', None)
        new_image_url = utils.upload_thumbnail(thumbnail_image)

        trailer_video = self.cleaned_data.get('trailer_video', None)
        new_trailer_url = utils.upload_trailer(trailer_video)

        self.instance.image_url = new_image_url
        self.instance.trailer_url = new_trailer_url
        self.instance.created_at = utils.jkt_now()
        self.instance.updated_at = utils.jkt_now()
        
        return super().save(commit)


    class Meta:
        model = Courses
        exclude = ["image_url", "trailer_url", "updated_at", "created_at", "deleted_at"]