'''
Inderpreet Singh
015321384
CMPE131 HW3
'''
from flask import Flask, flash, redirect, render_template, request, session, abort

myapp_obj = Flask(__name__)

name = "Inder"
city_names = ['Paris', 'Denver', 'Rome', 'Delhi']

@myapp_obj.route("/")
def home():
	html_code =  '''
	<html>
	<body>
		<h1>Welcome ''' + name + ''' </h1>
		<a href="google.com"> not google</a>
		<p>
		</ul>'''
	for i in city_names:
		 html_code += '''<li> ''' + i 
	final_html_code = html_code + '''</li></ul></body></html>'''
	return final_html_page

#myapp_obj.run()

'''
Discussed this question with Christian (classmate) and used the lecture slides for reference
'''
