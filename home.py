'''
Inderpreet Singh
015321384
CMPE131 HW3
'''
from flask import Flask, flash, redirect, render_template, request, session, abort

myapp_obj = Flask(__name__)

name = "Inder"
city_names = ['Paris', 'Denver', 'Rome', 'Delhi']

iter = lambda : for i in city_names
@myapp_obj.route("/")
def home():
	return '''
	<html>
	<body>
		<h1>Welcome ''' + name + ''' </h1>
		<a href="https://google.com"> not google</a>
		<ul>
			<li> ''' + iter + ''' </li>
		</ul>
	</body>
	</html>

#myapp_obj.run()

'''
Discussed this question with Christian (classmate) and used the lecture slides for reference
'''
