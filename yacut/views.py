from flask import flash, redirect, render_template

from . import app
from .forms import URLForm
from .models import URLMap
from .utils import validate_short_id, create_url_map


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short, error = validate_short_id(
        form.custom_id.data, f'Имя {form.custom_id.data} уже занято!'
    )
    original = form.original_link.data
    if error is not None:
        flash(error)
        return render_template('index.html', form=form)
    create_url_map(original, short)
    flash('Ваша новая ссылка готова:')
    flash(short)
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def jump(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
