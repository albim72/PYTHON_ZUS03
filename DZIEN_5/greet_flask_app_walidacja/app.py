from flask import Flask, render_template, request, redirect, url_for
from person import Person

app = Flask(__name__)

# Lista osób
people_list = [
    Person(1,"Anna",28),
    Person(2,"Olaf",35),
    Person(3,"Nadia",78),
    Person(4,"Leon",57)
]
next_id=5

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id

    greeting_name = None
    error_message = None

    # Obsługa formularza powitania
    if request.method == 'POST' and 'name' in request.form:
        greeting_name = request.form.get('name')

    # Obsługa formularza dodawania osoby
    if request.method == 'POST' and 'new_name' in request.form:
        new_name = request.form.get('new_name', '').strip()
        new_age = request.form.get('new_age', '').strip()

        if not new_name:
            error_message = "Imię nie może być puste."
        elif not new_age.isdigit():
            error_message = "Wiek musi być liczbą całkowitą."
        elif int(new_age) < 0:
            error_message = "Wiek nie może być ujemny."
        else:
            age = int(new_age)
            people_list.append(Person(next_id, new_name, age))
            next_id += 1
            return redirect(url_for('index'))

    people = [p.to_dict() for p in people_list]
    return render_template('index.html', name=greeting_name, people=people, error=error_message)

