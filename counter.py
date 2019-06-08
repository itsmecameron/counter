from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'let me whisper in your ear'

@app.route('/')
def index(): 
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    if 'count2' in session:
        session['count2'] = session.get('count2') + 1
    else:
        session['count2'] = 1
    return render_template("counter.html", count = session['count'], count2 = session['count2'])
    
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

@app.route('/<x>')
def input(x):
    num = int(x)
    session['count'] = num
    return redirect('/')

@app.route('/add')
def add():
    session['count'] = session['count'] + 1 
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)