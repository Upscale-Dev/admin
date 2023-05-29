import pytz
from datetime import datetime

from course.custom_storage import ImageStorage, ThumbnailStorage, TrailerStorage, VideoStorage


def upload_image(image_file):
    image_storage = ImageStorage()
    image_storage_name = image_file.__str__()
    image_storage.save(image_storage_name, image_file)
    new_image_url = image_storage.url(image_storage)
    return new_image_url


def upload_thumbnail(thumbnail_image):
    thumbnail_storage = ThumbnailStorage()
    thumbnail_image_name = thumbnail_image.__str__()
    thumbnail_storage.save(thumbnail_image_name, thumbnail_image)
    new_thumbnail_url = thumbnail_storage.url(thumbnail_image_name)
    return new_thumbnail_url


def upload_trailer(trailer_video):
    trailer_storage = TrailerStorage()
    trailer_video_name = trailer_video.__str__()
    trailer_storage.save(trailer_video_name, trailer_video)
    new_trailer_url = trailer_storage.url(trailer_video_name)
    return new_trailer_url


def upload_main_video(main_video):
    video_storage = VideoStorage()
    video_storage_name = main_video.__str__()
    video_storage.save(video_storage_name, main_video)
    new_video_url = video_storage.url(video_storage_name)
    return new_video_url


def jkt_now():
    tz_jkt = pytz.timezone('Asia/Jakarta')
    datetime_jkt = datetime.now(tz_jkt)
    return datetime_jkt
