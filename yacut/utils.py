import string
import random

from . import db
from .error_handlers import InvalidAPIUsage
from .models import URLMap

ALLOWED_CHARS = string.ascii_letters + string.digits


def get_unique_short_id():
    return ''.join((random.choice(ALLOWED_CHARS) for i in range(6)))


def check_string(value):
    for letter in value:
        if letter not in ALLOWED_CHARS:
            return True
    return False


def check_len(value):
    if len(value) > 16:
        return True


def validate_short_id(short, error_massage):
    if short is None or short == '':
        return get_unique_short_id(), None
    if check_string(short):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки', 400
        )
    if check_len(short):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки', 400
        )

    if bool(URLMap.query.filter_by(short=short).first()):
        return short, f'{error_massage}'
    return short, None


def create_url_map(original, short):
    urlmap = URLMap(
        original=original,
        short=short,
    )
    db.session.add(urlmap)
    db.session.commit()
