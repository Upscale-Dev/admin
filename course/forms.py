from typing import Any
from django import forms

from course import utils
from course.models import Courses


class CourseAdminForm(forms.ModelForm):
    image_file = forms.FileField(label="Image File", required=True)
    trailer_video = forms.FileField(label="Trailer Video", required=True)
    files = forms.FileField(label="Files", required=True)

    def save(self, commit=True) -> Any:
        image_file = self.cleaned_data.get('image_file', None)
        new_image_url = utils.upload_image(image_file)

        trailer_video = self.cleaned_data.get('trailer_video', None)
        new_trailer_url = utils.upload_trailer(trailer_video)

        files = self.cleaned_data.get('files', None)
        new_files_url = utils.upload_files(files)

        self.instance.image_url = new_image_url
        self.instance.trailer_url = new_trailer_url
        self.instance.files = new_files_url
        self.instance.created_at = utils.jkt_now()
        self.instance.updated_at = utils.jkt_now()

        return super().save(commit)

    class Meta:
        model = Courses
        exclude = ["image_url", "trailer_url",
                   "updated_at", "created_at", "deleted_at"]


class VideoAdminForm(forms.ModelForm):
    thumbnail_image = forms.FileField(label="Thumbnail Image", required=True)
    main_video = forms.FileField(label="Main Video", required=True)

    def save(self, commit=True) -> Any:
        thumbnail_image = self.cleaned_data.get('thumbnail_image', None)
        new_thumbnail_url = utils.upload_thumbnail(thumbnail_image)

        main_video = self.cleaned_data.get('main_video', None)
        new_main_url = utils.upload_main_video(main_video)

        self.instance.thumbnail_url = new_thumbnail_url
        self.instance.main_url = new_main_url

        return super().save(commit)

    class Meta:
        model = Courses
        exclude = ["thumbnail_url", "main_url"]
