from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, DecimalField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jshgiusdnsdghs&"*(^$uefiaoheio£^ahgljf27380,.>><?@@!oaghvioejiah'

class BasicForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    dob = DateField('D.O.B: ', format='%d/%m/%Y')
    age = IntegerField('Enter Age: ')
    salary = DecimalField('Enter Salary: ', places=2)
    formation = SelectField('Select Formation: ', choices = [("3-4-3"), ("4-4-2"), ("4-5-1")])
    submit = SubmitField('Add')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        age = form.age.data
        salary = form.salary.data
        formations = form.formation.data


        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return f'{first_name} {last_name}, you have chosen {formations} as your formation. Here is you DoB: {dob}. You are {age} years old and have a salary of - {salary}.'

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')