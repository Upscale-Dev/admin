import pytz
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
