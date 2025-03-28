from flask import Flask,render_template,request
from person import Person

app = Flask(__name__)

people_list = [
    Person(1,"Anna",28),
    Person(2,"Olaf",35),
    Person(3,"Nadia",78),
    Person(4,"Leon",57)
]

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    people = [p.to_dict() for p in people_list]
    return render_template('index.html',name=name,people=people)

if __name__ == '__main__':
    app.run(debug=True)
