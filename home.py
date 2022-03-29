from flask import Flask, flash, redirect, render_template, request, session, abort

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def hello():
	name = "Inder"
	city_names = ['Paris', 'Denver', 'Rome', 'Delhi']
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

myapp_obj.run()

