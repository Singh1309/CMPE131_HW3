from app import myobj
from flask import Flask, flash, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

class CityNamesForm(FlaskForm):
	city = StringField('City Name', validators=[DataRequired()])
	submit = SubmitField("Submit!")

@myobj.route("/", methods=('GET', 'POST'))
def home():
	form = CityNamesForm()
	if form.validate_on_submit():
		flash(format(form.city.data))
	return render_template('home.html', length=len(city_names), name=name, city_names=city_names, form=form)