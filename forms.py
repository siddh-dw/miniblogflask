from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)], render_kw={"placeholder": "Teclea tu nombre completo", 'class':'mt-4, form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Teclea tu nombre completo", 'class':'mt-4, form-control'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'class':'mt-4, form-control'})
    submit = SubmitField('Registrar', render_kw={'class':'btn btn-primary mt-4 mb-4', 'style':'float: right;'})

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)], render_kw={"placeholder": "", 'class':'mt-4, form-control'})
    title_slug = StringField('Subtitulo', validators=[Length(max=128)], render_kw={"placeholder": "", 'class':'mt-4, form-control'})
    content = TextAreaField('Contenido', render_kw={"placeholder": "", 'class':'mt-4, form-control'})
    submit = SubmitField('Enviar', render_kw={'class':'btn btn-primary mt-4 mb-4', 'style':'float: right;'})