# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:54:03 2018

@author: Saverio
"""

from flask import Flask, request, render_template, flash, redirect, url_for, sessions, logging
from data import Entries
from flaskext.mysql import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms.widgets import TextArea
from passlib.hash import sha256_crypt


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'eventLogDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

entries = Entries()


''' -------------- Routes -----------------'''

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/dashboard')
def dashboard():
	return(render_template('dashboard.html'))

@app.route('/summary')
def summary():
	return(render_template('summary.html'))

@app.route('/howto')
def howto():
	return(render_template('howto.html'))

@app.route('/viewList')
def viewList():
	return(render_template('viewList.html', entries = entries))

@app.route('/entry/<string:id>/')
def viewEntry(id):
	return(render_template('viewEntry.html', id = id))

@app.route('/insert', methods=['GET', 'POST'])
def insertEvent():
	formInsert = InsertEntryForm(request.form)
	if request.method == 'POST' and form.validate():
        # if the submit button is pressed handle the data coming from the form
		return(render_template('insert.html'))
	return(render_template('insert.html', form=formInsert))

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		return(render_template('register.html'))
	return(render_template('register.html', form=form))

''' ---------------- Forms -------------------'''

# Form per la registrazione degli utenti
class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
			validators.DataRequired(),
			validators.EqualTo('confirm', message='password do not match')
		])
	confirm = PasswordField('Confirm password')

class InsertEntryForm(Form):
    #newEntry = StringField('Log', widget=TextArea())
	newEntry = StringField('Log', [validators.Length(min=3, max=360)])

if __name__ == '__main__':
    app.run()
