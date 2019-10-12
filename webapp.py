from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/address', methods = ['POST'])
def address():
	postcode = request.form['postcode']
	print(postcode)
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') 
