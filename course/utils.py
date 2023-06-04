import pytz
from datetime import datetime

from course.custom_storage import ImageStorage, ThumbnailStorage, TrailerStorage, VideoStorage, FilesStorage


def upload_image(image_file):
    image_storage = ImageStorage()
    image_storage_name = generate_file_name(image_file.__str__())
    image_storage.save(image_storage_name, image_file)
    new_image_url = image_storage.url(image_storage_name)
    return new_image_url


def upload_thumbnail(thumbnail_image):
    thumbnail_storage = ThumbnailStorage()
    thumbnail_image_name = generate_file_name(thumbnail_image.__str__())
    thumbnail_storage.save(thumbnail_image_name, thumbnail_image)
    new_thumbnail_url = thumbnail_storage.url(thumbnail_image_name)
    return new_thumbnail_url


def upload_trailer(trailer_video):
    trailer_storage = TrailerStorage()
    trailer_video_name = generate_file_name(trailer_video.__str__())
    trailer_storage.save(trailer_video_name, trailer_video)
    new_trailer_url = trailer_storage.url(trailer_video_name)
    return new_trailer_url


def upload_main_video(main_video):
    video_storage = VideoStorage()
    video_storage_name = generate_file_name(main_video.__str__())
    video_storage.save(video_storage_name, main_video)
    new_video_url = video_storage.url(video_storage_name)
    return new_video_url

def upload_files(files):
    files_storage = FilesStorage()
    files_storage_name = generate_file_name(files.__str__())
    files_storage.save(files_storage_name, files)
    new_files_url = files_storage.url(files_storage_name)
    return new_files_url

def generate_file_name(file_name):
    file_extension = file_name.split(".")[-1]
    file_name = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}.{file_extension}"
    return file_name

def jkt_now():
    tz_jkt = pytz.timezone('Asia/Jakarta')
    datetime_jkt = datetime.now(tz_jkt)
    return datetime_jkt
