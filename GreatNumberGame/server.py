from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'my_key'

@app.route('/', methods=['POST','GET'])
def index():
  import random
  session['myNumber'] = random.randrange(0, 101)
  return render_template("index.html")

@app.route('/compare', methods=['POST'])
def compare():
    myNumber =  int(session['myNumber'])
    print myNumber
    guess = int(request.form['guess'])
    if guess < myNumber:
        low_high = 'Too Low!'
    elif guess > myNumber:
        low_high = 'Too High!'
    elif guess == myNumber:
        low_high = 'You got it! ' + str(myNumber) + ' was the number!'
        return render_template('playAgain.html', low_high = low_high)
    return render_template("compare.html", low_high = low_high)

@app.route('/again', methods=['POST', 'GET'])
def again():
    return redirect('/')

app.run(debug=True) # run our server
