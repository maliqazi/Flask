from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
  s_first_name = str(request.form['first_name'])
  s_last_name = str(request.form['last_name'])
  if (len(request.form['email']) < 1 or
        len(request.form['first_name']) < 1 or
        len(request.form['last_name']) < 1 or
        len(request.form['password']) < 1 or
        len(request.form['confirm_password']) < 1):
    flash(u'Please complete all fields','error')
  else:
    if  not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid email address','error')
    elif len(request.form['password']) < 8:
        flash(u'Create a password longer than 8 characters','error')
    elif request.form['password'] != request.form['confirm_password']:
        flash(u'Password does not match','error')
    elif str.isalpha(s_first_name)  == False or str.isalpha(s_last_name) == False:
        flash(u'First and Last names can only contain alphabets','error')
    else:
        flash(u'Thanks for submitting your information','success')

  return redirect('/')

app.run(debug=True)
