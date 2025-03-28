from flask import Flask,render_template,request,redirect,url_for
from person import Person

app = Flask(__name__)

people_list = [
    Person(1,"Anna",28),
    Person(2,"Olaf",35),
    Person(3,"Nadia",78),
    Person(4,"Leon",57)
]
next_id=5
@app.route('/',methods=['GET','POST'])
def index():
    global next_id

    #obsługa formularza powitania
    greeting_name = None
    if request.method == 'POST' and 'name' in request.form:
        greeting_name = request.form.get('name')

    #obsługa formularza dodawania osoby
    if request.method == 'POST' and 'new_name' in request.form:
        new_name = request.form.get('new_name')
        new_age = request.form.get('new_age')

        if new_name and new_age:
            try:
                age = int(new_age)
                people_list.append(Person(next_id,new_name,age))
                next_id += 1
                return redirect(url_for('index'))
            except ValueError:
                pass
    people = [p.to_dict() for p in people_list]
    return render_template('index.html',name=greeting_name,people=people)

if __name__ == '__main__':
    app.run(debug=True)
