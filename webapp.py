from flask import Flask, render_template, request, redirect
from datetime import datetime 

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/address', methods = ['POST'])
def address():
	postcode = request.form['postcode']
	print(postcode)
	# TODO input data into scraper methods and return data
	data = [['Tuesday', '01', 'General'], ['Tuesday', '08', 'General'], ['Thursday', '10', 'Recycling'], ['Thursday', '10', 'Glass'], ['Tuesday', '15', 'General'], ['Tuesday', '22', 'General'], ['Thursday', '24', 'Recycling'], ['Thursday', '24', 'Glass'], ['Tuesday', '29', 'General']]

	return render_template("index.html", data=data, month=datetime.now().strftime('%b'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') 
