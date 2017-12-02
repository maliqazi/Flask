from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key='mykey'

@app.route("/", methods = ['POST','GET'])
def index():
    session['number'] += 1
    return render_template('index.html', number =session['number'])
app.run()
