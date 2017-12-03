from flask import Flask, render_template, request, redirect,session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comments = request.form['comments']
   if len(name) < 1 or len(comments) < 1:
       flash("Name and comments cannot be empty!")
   elif len(comments) > 120:
       flash("Comments should be 120 characters or less")
   else:
       return render_template("result.html",name=name,location=location,language=language,comments=comments)
   return redirect('/')

@app.route('/redir')
def redir():
    print "Redirecting to index.html"
    return redirect('/')

app.run(debug=True)
