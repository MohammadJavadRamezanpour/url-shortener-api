import random
import string

from shortener.models import Link
from config.settings import RANDOM_KEY_LENGTH
# this was also correct -> from django.conf import settings and then settings.RANDOM_KEY_LENGTH

def get_random_string():
    """Generate a random string of specified length."""
    length = RANDOM_KEY_LENGTH
    letters_and_digits = string.ascii_lowercase + string.digits

    while True:
        key = ''.join(random.choice(letters_and_digits) for i in range(length))

        if not Link.objects.filter(key=key).exists():
            return key




