
from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:645202398@34.121.192.21/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


@app.route('/')
def homey():
    return '<html><head><h2><center>Head of<center></h2></head><body style="background-color:blue"><br><hr><br><b>Dan</b></body></html>'


if __name__=='__main__':
    app.run(debug=True)
