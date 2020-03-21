from flask import Flask, render_template, request, send_file
from flask_restful import reqparse, Api, Resource
import os
import multi_task
import twee
app = Flask(__name__)
@app.route('/')
def home_page():
	return render_template("dai_twee.html")

@app.route('/', methods = ['POST'])
def post():
	d=[]
	d.append(str(request.form['one']))
	d.append(str(request.form['two']))
	d.append(str(request.form['three']))
	d.append(str(request.form['four']))
	s = ""
	for i in d: s = s+" "+i
	if '' in d: return "Wrong Input"
	os.system("python3 multi_task.py"+s)
	print("python3 multi_task.py"+s)
	return send_file('daily.zip', mimetype='zip',attachment_filename='daily.zip',as_attachment=True)

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 80, debug=True)
