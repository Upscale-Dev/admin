from typing import Any
from django import forms
from django.core.validators import FileExtensionValidator

from course import utils
from course.models import Courses


class CourseAdminForm(forms.ModelForm):
    image_file = forms.FileField(label="Image File", required=True, validators=[utils.image_type_validator])
    trailer_video = forms.FileField(label="Trailer Video", required=True, validators=[utils.video_type_validator])
    files = forms.FileField(label="Files", required=True, validators=[utils.document_type_validator])

    def save(self, commit=True) -> Any:
        image_file = self.cleaned_data.get('image_file', None)
        new_image_url = utils.upload_object(image_file)

        trailer_video = self.cleaned_data.get('trailer_video', None)
        new_trailer_url = utils.upload_object(trailer_video)

        files = self.cleaned_data.get('files', None)
        new_files_url = utils.upload_object(files)

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

class CourseAdminEditForm(forms.ModelForm):
    image_file = forms.FileField(label="Image File", required=False, validators=[utils.image_type_validator])
    trailer_video = forms.FileField(label="Trailer Video", required=False, validators=[utils.video_type_validator])
    files = forms.FileField(label="Files", required=False, validators=[utils.document_type_validator])

    def save(self, commit=True) -> Any:
        image_file = self.cleaned_data.get('image_file', None)
        if image_file:
            self.instance.image_url = utils.upload_object(image_file)

        trailer_video = self.cleaned_data.get('trailer_video', None)
        if trailer_video:
            self.instance.trailer_url = utils.upload_object(trailer_video)


        files = self.cleaned_data.get('files', None)
        if files != self.instance.files:
            self.instance.files = utils.upload_object(files)

        self.instance.updated_at = utils.jkt_now()

        return super().save(commit)

    class Meta:
        model = Courses
        exclude = ["image_url", "trailer_url",
                   "updated_at", "created_at", "deleted_at"]


class VideoAdminForm(forms.ModelForm):
    thumbnail_image = forms.FileField(label="Thumbnail Image", required=True, validators=[utils.image_type_validator])
    main_video = forms.FileField(label="Main Video", required=False, validators=[utils.video_type_validator])

    def save(self, commit=True) -> Any:
        thumbnail_image = self.cleaned_data.get('thumbnail_image', None)
        new_thumbnail_url = utils.upload_object(thumbnail_image)

        main_video = self.cleaned_data.get('main_video', None)
        new_main_url = utils.upload_object(main_video)

        self.instance.thumbnail_url = new_thumbnail_url
        self.instance.main_url = new_main_url

        return super().save(commit)

    class Meta:
        model = Courses
        exclude = ["thumbnail_url", "main_url"]


class VideoAdminEditForm(forms.ModelForm):
    thumbnail_image = forms.FileField(label="Thumbnail Image", required=False, validators=[utils.image_type_validator])
    main_video = forms.FileField(label="Main Video", required=False, validators=[utils.video_type_validator])

    def save(self, commit=True) -> Any:
        thumbnail_image = self.cleaned_data.get('thumbnail_image', None)
        if thumbnail_image:
            self.instance.thumbnail_url = utils.upload_object(thumbnail_image)


        main_video = self.cleaned_data.get('main_video', None)
        if main_video:
            self.instance.main_url = utils.upload_object(main_video)

        return super().save(commit)

    class Meta:
        model = Courses
        exclude = ["thumbnail_url", "main_url"]
