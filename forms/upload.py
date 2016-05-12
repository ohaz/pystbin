from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

from app import lexers

__author__ = 'ohaz'


class TextUploadForm(Form):
    title = StringField('title')
    text = TextAreaField('text', validators=[DataRequired()])
    language = SelectField('language', choices=[(a, a) for a in lexers.keys()])
    hllines = StringField('hllines')

    def to_dict(self):
        return {'title': self.title.data, 'type': 'text', 'language': self.language.data,
                'hllines': self.hllines.data.split(',')}
