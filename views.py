import random
import string

from app import app, lexers, auth_key, basepath
from flask import render_template, abort, redirect, url_for
from pygments import highlight
from pygments.lexers import *
from pygments.formatters import HtmlFormatter
import json
import os

from forms.upload import TextUploadForm

__author__ = 'ohaz'


@app.route('/s/<p_id>/')
def show(p_id):
    data = None
    try:
        json_data = open(os.path.join(basepath, 'uploads', p_id + '.json')).read()
        data = json.loads(json_data)
    except (OSError, IOError) as e:
        abort(404)
    if data['type'] == 'text':
        code = open(os.path.join(basepath, 'uploads', 'files', p_id)).read()
        return render_template('show.html', title=data['title'], language=data['language'],
                               code=highlight(code, lexers[data['language']](),
                                              HtmlFormatter(linenos='table', hl_lines=data['hllines'])))


@app.route('/u/<key>', methods=['POST'])
def up(key):
    if key == auth_key:
        form = TextUploadForm()
        name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
        while os.path.exists(os.path.join(basepath, 'uploads', name+'.json')):
            name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
        upload_dict = form.to_dict()
        upload_text = form.text.data
        with open(os.path.join(basepath, 'uploads', name+'.json'), 'a+') as f:
            json.dump(upload_dict, f)
        with open(os.path.join(basepath, 'uploads', 'files', name), 'a+') as f:
            f.write(upload_text)
        return redirect(url_for('show', p_id=name))
    else:
        abort(401)
