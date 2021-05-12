from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, DecimalField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jshgiusdnsdghs&"*(^$uefiaoheio£^ahgljf27380,.>><?@@!oaghvioejiah'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = DateField('Date of Birth')
    usernumber = IntegerField('Enter Number')
    userdec = DecimalField('Enter Decimal Number')
    dropdown = SelectField('Select Formation', choices = [("3-4-3"), ("4-4-2"), ("4-5-1")])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        formationlist = form.dropdown.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return f'{first_name} {last_name}, you have chosen {formationlist} as your formation.'

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')