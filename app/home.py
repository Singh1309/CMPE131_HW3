'''
Inderpreet Singh
015321384
CMPE131 HW3
'''
from flask import Flask, flash, redirect, render_template, request, session, abort

myapp_obj = Flask(__name__)

name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myapp_obj.route("/")
def home():
	html_code =  '''
	<html>
	<body>
		<h1>WelcomeLisa!</h1>
		<ahref="www.google.com"> not google</a>
		<p>
		<ul>'''
	for i in city_names:
		 html_code += '''<li>''' + i
	final_html_code = html_code + '''</li></ul></p></body></html>'''
	return final_html_code

#myapp_obj.run()