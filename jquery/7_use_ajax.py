from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        return jsonify({'message': 'This is a GET response'})
    
    if request.method == 'POST':
        data = request.json
        return jsonify({'received': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

