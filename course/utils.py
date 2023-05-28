from datetime import datetime
import pytz

def jkt_now():
    tz_jkt = pytz.timezone('Asia/Jakarta') 
    datetime_jkt = datetime.now(tz_jkt)
    return datetime_jkt