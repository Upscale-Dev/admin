import pytz
import os
from django.core.exceptions import ValidationError

from datetime import datetime
from django.conf import settings

from course.custom_storage import R2Storage

def upload_object(file):
    storage = R2Storage()
    file_storage_name = generate_file_name(file.__str__())
    storage.save(file_storage_name, file)
    r2_url = getattr(settings, "R2_PUBLIC_URL", "content.bizbzt.com")
    file_url = f"{r2_url}/{file_storage_name}"
    return file_url
    

def generate_file_name(file_name):
    file_extension = file_name.split(".")[-1]
    file_name = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}.{file_extension}"
    return file_name

def jkt_now():
    tz_jkt = pytz.timezone('Asia/Jakarta')
    datetime_jkt = datetime.now(tz_jkt)
    return datetime_jkt

def video_type_validator(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    video_extensions = [
        ".mp4",
        ".avi",
        ".mkv",
        ".mov",
        ".wmv",
        ".flv",
        ".m4v",
        ".webm",
        ".mpeg",
        ".mpg",
        ".3gp",
        ".ogv",
        ".qt",
        ".rm",
        ".vob",
        ".m2v",
        ".mpg",
        ".divx",
    ]
    if not ext.lower() in video_extensions:
        raise ValidationError(f"Video File Extensions Supported:{video_extensions}")
    return

def image_type_validator(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    image_extensions = [
    ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".svg",
        ".tif",
        ".tiff",
        ".webp",
        ".ico"
    ]
    if not ext.lower() in image_extensions:
        raise ValidationError(f"Image File Extensions Supported:{image_extensions}")
    return


def document_type_validator(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    document_extensions = [
        ".doc",
        ".docx",
        ".pdf",
        ".txt",
        ".csv",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".odt",
        ".ods"
    ]
    if not ext.lower() in document_extensions:
        raise ValidationError(f"File Extensions Supported:{document_extensions}")
    return
