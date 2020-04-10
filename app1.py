from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form['data']
    key_pressed = request.form['key_pressed']
    data = data.lower()
    if key_pressed=="enter_key":
    	data = data[0: len(data)-1] #solve for send key
    global_name = "I'm Shaily"
    #algo to start from here
    if data:
    	data_l = data.split(" ")
    	if "your" in data_l and "name" in data_l:
    		return jsonify({'answer':global_name})
    	if "how" in data_l and "you" in data_l:
    		return jsonify({'answer':"I'm Good and wish for your well being!"})
    	data_ = data[::-1]
    	
    	return jsonify({'answer':data_})
    else:
    	return jsonify({'error':"Missing data"})