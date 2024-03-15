from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectMultipleField, TextAreaField, SubmitField, widgets
from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
class FeedbackForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone')
    experience = RadioField('What do you think of your experience at GIC?',
                            choices=[('perfect', 'Perfect'), ('good', 'Good'),
                                     ('normal', 'Normal'), ('poor', 'Poor')],
                            validators=[DataRequired()])
    improvement = MultiCheckboxField('Improvement of GIC', choices=[
                            ('Resources and Facilities', 'Resources and Facilities'),
                            ('Academic Support', 'Academic Support'),
                            ('Course Availability and Variety', 'Course Availability and Variety'),
                            ('Campus Life and Student Engagement', 'Campus Life and Student Engagement'),
                            ('Already good', 'Already good')],
                             validators=[DataRequired()])

    additional_feedback = TextAreaField('Please provide any additional comments or feedback:',
                                        validators=[DataRequired()])
    submit = SubmitField('Submit')