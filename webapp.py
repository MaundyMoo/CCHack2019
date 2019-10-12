from flask import Flask, render_template, request, redirect
from datetime import datetime 
import webparser

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/address', methods = ['POST'])
def address():
	postcode = request.form['postcode']
	print(postcode)
	# TODO input data into scraper methods and return data
	data = webparser.parse_address(postcode)
	data = webparser.parse_data(data)
	return render_template("index.html", data=data, month=datetime.now().strftime('%b'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') 
