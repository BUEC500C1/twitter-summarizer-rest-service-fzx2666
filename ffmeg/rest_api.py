from flask import Flask, render_template, request, send_file
from flask_restful import reqparse, Api, Resource
import os
import multi_task

app = Flask(__name__)
@app.route('/')

def home_page():
	multi_task.ThreadHw4()
	return render_template("dai_twee.html")

def upload():
	return send_file('daily.zip', mimetype='zip',attachment_filename='daily.zip',as_attachment=True)

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 80, debug=True)