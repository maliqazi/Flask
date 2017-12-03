from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'my_key'

#session['total_gold'] = 0

@app.route('/', methods=['POST','GET'])
def index():
  #total_gold = 0
  #session['total_gold'] = total_gold
  #session['activities'] = ''
  return render_template("index.html")#, total_gold = session['total_gold'], activities = session['activities'])

@app.route('/process_money', methods=['POST'])
def process():
    import random
    if request.form['building'] == 'farm':
        goldAttained = random.randrange(10, 20)
        print goldAttained
        session['total_gold'] += goldAttained
        print session['total_gold']
        session['activities'] += 'Earned ' + str(goldAttained) + ' golds from the farm\n'
    elif request.form['building'] == 'cave':
        goldAttained = random.randrange(5, 10)
        print goldAttained
        session['total_gold'] += goldAttained
        print session['total_gold']
        session['activities'] += 'Earned ' + str(goldAttained) + ' golds from the cave\n'
    elif request.form['building'] == 'house':
        goldAttained = random.randrange(2, 5)
        print goldAttained
        session['total_gold'] += goldAttained
        print session['total_gold']
        session['activities'] += 'Earned ' + str(goldAttained) + ' golds from the house\n'
    elif request.form['building'] == 'casino':
        goldAttained = random.randrange(-50, 50)
        print goldAttained
        session['total_gold'] += goldAttained
        print session['total_gold']
        session['activities'] += 'Entered a caino and ' + str(goldAttained) + '\n'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['total_gold']=0
    session['activities']=''
    return redirect('/')

app.run(debug=True)
