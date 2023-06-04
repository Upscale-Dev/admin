from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class ImageStorage(S3Boto3Storage):
    bucket_name = getattr(settings, "R2_IMAGE_BUCKET", "images")


class ThumbnailStorage(S3Boto3Storage):
    bucket_name = getattr(settings, "R2_THUMBNAIL_BUCKET", "thumbnails")


class TrailerStorage(S3Boto3Storage):
    bucket_name = getattr(settings, "R2_TRAILER_BUCKET", "trailers")


class VideoStorage(S3Boto3Storage):
    bucket_name = getattr(settings, "R2_VIDEO_BUCKET", "videos")

class FilesStorage(S3Boto3Storage):
    bucket_name = getattr(settings, "R2_FILES_BUCKET", "files")