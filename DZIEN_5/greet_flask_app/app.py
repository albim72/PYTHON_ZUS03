from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    people = [
        {"id":1,"name":"Anna","age":28},
        {"id":2,"name":"Olaf","age":66},
        {"id":3,"name":"Nadia","age":38},
        {"id":4,"name":"Leon","age":23}
    ]
    return render_template('index.html',name=name,people=people)

if __name__ == '__main__':
    app.run(debug=True)
