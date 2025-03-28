from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    name = request.args.get('name','World')
    return jsonify({'message':f'Hello, {name}!'})

@app.route('/add', methods=['POST'])
def add():
    if request.is_json:
        data = request.get_json()
        a = data.get('a', 0)
        b = data.get('b', 0)
    else:
        a = request.form.get('a', 0)
        b = request.form.get('b', 0)

    try:
        a = float(a)
        b = float(b)
        return jsonify({'result': a + b})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
