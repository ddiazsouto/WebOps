
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='Key22'


class BasicForm(FlaskForm):

    login = StringField('Your name here please')
    passwd= StringField('And your password')
    submit= SubmitField('Log in')


db=SQLAlchemy(app)




@app.route('/', methods=['GET', 'POST'])
def homey():
    return render_template('main.html', title='Home')

@app.route('/room', methods=['POST', 'GET'])
def login():

    Truekey='GorradeGorrin'
    msg=''

    form = BasicForm()

    if request.method=='POST':
        
        login = form.login.data
        passwd= form.passwd.data

        if passwd == 'GorradeGorrin':
            return render_template('room1.html', user=login, title= 'Welcome', login=login)

        else:
            msg = 'Sorry, those login details are not correct, try again'


    return render_template('room.html', title='Login Menu', form=form, message=msg)

    

if __name__=='__main__':
    app.run(debug=True)
