from flask import Flask, render_template, request, send_file
from flask_restful import reqparse, Api, Resource
import os
import multi_task

app = Flask(__name__)
@app.route('/get_daily')

def upload():
	multi_task.ThreadHw4()
	return send_file('daily.zip', mimetype='zip',attachment_filename='daily.zip',as_attachment=True)
	#return "hello world!"
#api.add_resource(multi_task,'/daily')

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 80, debug=True)
