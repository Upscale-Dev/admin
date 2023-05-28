from storages.backends.s3boto3 import S3Boto3Storage

class ThumbnailStorage(S3Boto3Storage):
    bucket_name = "thumbnails"

class TrailerStorage(S3Boto3Storage):
    bucket_name = "trailers"

class VideoStorage(S3Boto3Storage):
    bucket_name = "videos"