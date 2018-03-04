import random
import string
import uuid
import re
import datetime
from django.utils.html import strip_tags

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def rand_uid():
    return str(uuid.uuid4())[:8]

def count_words(html_string):
    word_string = strip_tags(html_string)
    count = len(re.findall(r'\w+'), word_string)
    return count

def get_read_time(html_string):
    count = count_words(html_string)
    read_time_in_min = (count/200.0)
    read_time_in_sec = read_time_in_min * 60
    read_time = str(datetime.timedelta(seconds=read_time_in_sec))
    return read_time
    