from flask_wtf import FlaskForm
from wtforms import SelectField,TextAreaField,SubmitField,StringField
from wtforms.validators import Required

class BlogForm(FlaskForm):
  title = StringField('Blog title')
  category = SelectField("Choose Category",choices=[('Lifestyle','LifeStyle'),('Fitness','Health & Fitness'),('Trending','Trends'),('IT','Technology')])
  blog_post = TextAreaField('Write Blog',validators=[Required()])
  writer = StringField('Your alias name')
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio =TextAreaField('Short description about you.',validators=[Required()])
  submit = SubmitField('Submit')

class CommentForm (FlaskForm):
  comment = StringField('Add your comment here',validators=[Required()])
  submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
  submit = SubmitField('Submit')

