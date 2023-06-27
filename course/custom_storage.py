from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class R2Storage(S3Boto3Storage):
    bucket_name = getattr(settings, "R2_BUCKET", "content")
