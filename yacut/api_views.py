from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import validate_short_id, create_url_map


@app.route('/api/id/', methods=('GET', 'POST'))
def create_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    original = data.get('url')
    if original is None or original == '':
        raise InvalidAPIUsage('"url" является обязательным полем!')

    short, error = validate_short_id(
        data.get('custom_id'), f'Имя "{data.get("custom_id")}" уже занято.'
    )
    if error:
        raise InvalidAPIUsage(error, HTTPStatus.BAD_REQUEST)
    create_url_map(original, short)

    result = {
        'short_link': f'{url_for("jump", short=short, _external=True)}',
        'url': original
    }
    return jsonify(result), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=('GET', ))
def get_original_url(short_id):
    original = URLMap.query.filter_by(short=short_id).first()
    if original is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': original.original}), HTTPStatus.OK
