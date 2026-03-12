from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Neha@2024'
app.config['MYSQL_DB'] = 'hospital_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['GET','POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        disease = request.form['disease']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients(name,age,gender,disease) VALUES(%s,%s,%s,%s)",
                    (name,age,gender,disease))
        mysql.connection.commit()
        cur.close()

        return redirect('/view_patients')

    return render_template('add_patient.html')


@app.route('/view_patients')
def view_patients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()
    cur.close()

    return render_template('view_patients.html', patients=data)


@app.route('/appointment', methods=['GET','POST'])
def appointment():
    if request.method == 'POST':
        patient = request.form['patient']
        doctor = request.form['doctor']
        date = request.form['date']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO appointments(patient_name,doctor_name,appointment_date) VALUES(%s,%s,%s)",
                    (patient,doctor,date))
        mysql.connection.commit()
        cur.close()

        return redirect('/')

    return render_template('appointment.html')


@app.route('/billing', methods=['GET','POST'])
def billing():
    if request.method == 'POST':
        patient = request.form['patient']
        treatment = request.form['treatment']
        amount = request.form['amount']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO billing(patient_name,treatment,amount) VALUES(%s,%s,%s)",
                    (patient,treatment,amount))
        mysql.connection.commit()
        cur.close()

        return redirect('/')

    return render_template('billing.html')


if __name__ == '__main__':
    app.run(debug=True)