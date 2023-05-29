from typing import Any
from django import forms

from course import utils
from course.models import Courses


class CourseAdminForm(forms.ModelForm):
    image_file = forms.FileField(label="Image File", required=True)
    trailer_video = forms.FileField(label="Trailer Video", required=True)

    def save(self, commit=True) -> Any:
        image_file = self.cleaned_data.get('image_file', None)
        new_image_url = utils.upload_image(image_file)

        trailer_video = self.cleaned_data.get('trailer_video', None)
        new_trailer_url = utils.upload_trailer(trailer_video)

        self.instance.image_url = new_image_url
        self.instance.trailer_url = new_trailer_url
        self.instance.created_at = utils.jkt_now()
        self.instance.updated_at = utils.jkt_now()

        return super().save(commit)

    class Meta:
        model = Courses
        exclude = ["image_url", "trailer_url",
                   "updated_at", "created_at", "deleted_at"]