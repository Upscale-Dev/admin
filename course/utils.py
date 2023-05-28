import pytz
from datetime import datetime

from course.custom_storage import ThumbnailStorage, TrailerStorage



def upload_thumbnail(thumbnail_image):
    thumbnail_storage = ThumbnailStorage()
    thumbnail_image_name = thumbnail_image.__str__()
    thumbnail_storage.save(thumbnail_image_name,thumbnail_image)
    new_image_url = thumbnail_storage.url(thumbnail_image_name)
    return new_image_url

def upload_trailer(trailer_video):
    trailer_storage  = TrailerStorage()
    trailer_video_name = trailer_video.__str__()
    trailer_storage.save(trailer_video_name, trailer_video)
    new_trailer_url = trailer_storage.url(trailer_video_name)
    return new_trailer_url


def jkt_now():
    tz_jkt = pytz.timezone('Asia/Jakarta') 
    datetime_jkt = datetime.now(tz_jkt)
    return datetime_jkt