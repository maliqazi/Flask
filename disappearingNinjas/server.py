from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key='mykey'

@app.route("/", methods = ['POST','GET'])
def index():
    return render_template('index.html')

@app.route("/ninja", methods = ['POST','GET'])
def ninja():
    return render_template('ninja.html', color='nocolor')

@app.route("/ninja/<color>", methods = ['POST','GET'])
def ninja_color(color):
    return render_template('ninja.html', color=color)
app.run(debug=True)
