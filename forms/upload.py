from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import HiddenInput

from app import lexers

__author__ = 'ohaz'


class TextUploadForm(Form):
    title = StringField('title')
    text = TextAreaField('text', validators=[DataRequired()])
    language = SelectField('language', choices=sorted([(a, a) for a in lexers.keys()]))
    hllines = StringField('hllines')
    api_call = StringField('api_call', widget=HiddenInput())

    def to_dict(self):
        return {'title': self.title.data, 'type': 'text', 'language': self.language.data,
                'hllines': self.hllines.data.split(',')}

    def is_api_call(self):
        return self.api_call.data == 'y'
