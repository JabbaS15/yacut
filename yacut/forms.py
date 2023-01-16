from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(
            Length(1, 256, message='Слишеом длинная ссылка'),
            DataRequired(message='Обязательное поле'),
            URL(message='Неккоректная ссылка')
        )
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=(
            Optional(),
            Length(max=16, message='Слишком длинное название'),
            Regexp(
                '^[A-Za-z0-9]*$',
                message='Можно использовать только латинские буквы и цифры'
            )
        )
    )
    submit = SubmitField('Создать')
