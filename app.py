
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("registration.html")
@app.route('/submit',methods=['POST'])
def hello():
    fname=request.form['fname']
    lname=request.form['lname']
    return render_template('greeting.html',fname=fname,lname=lname)
if (__name__=='__main__'):
    app.run(debug=True)