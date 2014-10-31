from pymongo import Connection
from flask import Flask, render_template,session,redirect

app= Flask(__name__)

@app.route("/")
def index():
    '''
    if 'n' not in session:
        session['n']=0
        
    n = session['n']
    n=n+1
    session['n']=n
    '''
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

'''
@app.route("/logout")
def logout():
    session.pop('n',None)
    return redirect("/")
'''

if __name__=="__main__":
    app.debug=True
    app.secret_key="Captian Swanson"
    app.run()
