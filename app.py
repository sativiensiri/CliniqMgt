from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import json
import os
from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv

load_dotenv()
database = os.getenv('DATABASE')


####### Function Space #######
def getDateTime():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d")
    current_time = current_datetime.strftime("%H:%M")
    date_time = current_date + "T" +current_time
    return date_time

def get_employee(userid):
    try:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM employee where userid = '{userid}'")
            columns = [column[0] for column in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            json_data = json.dumps(data, indent=4)
            jdata = json.loads(json_data)
            return jdata
    except:     # sqlite3.Error as error:
        return "0"

def get_registration(userid):
    try:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM registration where userid = '{userid}'")
            columns = [column[0] for column in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            json_data = json.dumps(data, indent=4)
            jdata = json.loads(json_data)
            return jdata
    except:     # sqlite3.Error as error:
        return "0"

def new_patient_id():
    fmt = "%Y%m%d%H%M%S"
    bangkok = datetime.now(timezone('Asia/Bangkok'))
    return bangkok.strftime(fmt)

####### End of Function  #######

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods = ['POST', 'GET'])
def index():
    return render_template("login.html")

@app.route("/registration", methods = ['POST', 'GET'])
def registration():
    session.pop('logged_in', False)
    session.pop('username', None)
    session.pop('role', None)

    if request.method == 'POST':
        # For Login
        if request.form.get('login-submit') == 'login':
            userid = request.form.get('login-username')
            password = request.form.get('login-password')
            employee = get_registration(userid)
            if len(employee) > 0:
                name = (employee[0]['name'])
                hashPassword = (employee[0]['password'])
                role = (employee[0]['department'])
                if check_password_hash(hashPassword, password):
                    session['logged_in'] = True
                    session['username'] = name
                    session['role'] = role
                    flash("Login Successful!", "success")
                    return redirect(url_for("services"))
                else:
                    flash("Check your password!", "danger")
                    return redirect(url_for("index"))
            else:
                flash("Employee not found!", "danger")
                return render_template("login.html")

        # For Register
        elif request.form.get('register-submit') == 'registration':
            userid = request.form.get('register-username').strip()
            password = request.form.get('register-password').strip()
            confirm_pass = request.form.get('confirm-password').strip()
            if (len(userid) > 0 and len(password) > 0 and len(confirm_pass) > 0):
                if password == confirm_pass:
                    hashPassword = generate_password_hash(password)
                    employees = get_employee(userid)
                    if len(employees) > 0:
                        date_time = getDateTime()
                        userid = (employees[0]['userid'])
                        name = (employees[0]['name'])
                        role = (employees[0]['department'])
                        sql = f"INSERT INTO registration VALUES ('{userid}', '{name}', '{role}', '{hashPassword}', '{date_time}')"
                        print(sql)
                        try:
                            with sqlite3.connect(database) as connection:
                                cursor = connection.cursor()
                                cursor.execute(sql)
                                connection.commit()
                            flash("Registration Successful!", "success")
                        except sqlite3.Error as error:
                            flash(f"Failed to insert data {error}", "danger")
                    else:
                        flash("Employee not found!", "danger")
                        return redirect(url_for("index"))
                else:
                    flash("Password and ConfirmPassword mismatch!", "danger")
            else:
                flash("Your UserID or Password too short, please provide a correcting!", "danger")
    else:
        flash("Please preform Login!", "danger")
        return redirect(url_for("index"))

@app.route("/services", methods = ['POST', 'GET'])
def services():
    if 'logged_in' in session:
        return render_template("services.html")
    else:
        return redirect(url_for("index"))

@app.route("/addnewpatient", methods = ['POST', 'GET'])
def addnewpatient():
    if 'logged_in' in session:
        if request.method == 'POST':
            new_patientId = new_patient_id()
            patientName = request.form.get('patient-name').strip()
            patientEmail = request.form.get('patient-email').strip()
            patientPhone = request.form.get('patient-phone').strip()
            patientAddress = request.form.get('patient-address').strip()
            patientCity = request.form.get('patient-city').strip()
            patientZp = request.form.get('patient-zipcode').strip()
            patientGender = request.form.get('patient-gender').strip()
            patientInfo = request.form.get('patient-info').strip()

            print(f"{new_patientId}  {patientName}  {patientEmail}  {patientPhone}  {patientAddress}  {patientCity}  {patientZp}  {patientGender}  {patientInfo}")
        return redirect(url_for("services"))
    else:
        return redirect(url_for("index"))


@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    if 'logged_in' in session:
        session.clear()
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()