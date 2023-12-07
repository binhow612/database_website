from flask import Flask, render_template, request, redirect, url_for
import fetch_data
import add_patient
import fetch_payment
import mysql.connector

app = Flask(__name__)
username = None
password = None
# doctor list for login
doctor_list = {
    "D00001": "00001",
    "D00002": "00002",
    "D00003": "00003",
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login_route(message=None):
    if request.method == "POST":
        try:
            data = request.form
            global username
            global password
            username = data['username']
            password = data['password']
            db = mysql.connector.connect(user=username, password=password, host="localhost", database="hospital")

            cursor = db.cursor()

            # Execute a SELECT query to fetch the user's data
            query = "SELECT * FROM doctor"
            cursor.execute(query)
            # Fetch the first row (if any)
            user_data = cursor.fetchall()

            # Check if a matching user was found
            if user_data:
                return redirect(url_for('homepage_route'))

        except Exception as e:
            # return render_template("login.html", message=f'Error: {str(e)}')
            return render_template("login.html", message='Invalid username or password.')
    return render_template("login.html", message='')
    
@app.route('/homepage')
def homepage_route():
    return render_template("homepage.html")

@app.route('/fetch_patient', methods = ['GET', 'POST'])
def fetch_patient_route():
    if (request.method == 'POST'):
        try:
            data = request.form
            code = data['code']
            type = data['patient_type']
            # Call the main function in fetch_data.py
            # result = fetch_data.fetch_data(username, password ,code, type="P")
            result = fetch_data.fetch_patient_data(username, password ,code, type)
            if result == "Error 1":
                message = f"Error 1: No patient found with code {code}"
            elif result == "Error 2":
                message = f"Invalid patient type for patient with code {code}"
            else:
                # message = {f'{key}':f'{value}' for key, value in result.items()}
                message = result
            return render_template("fetch_patient_data.html", message=message)

        except Exception as e:
            return render_template("fetch_patient_data.html", message=f'Error 3: {str(e)}')
    # For GET requests, simply render the page
    return render_template("fetch_patient_data.html", message='')

@app.route('/fetch_doctor', methods = ['GET', 'POST'])
def fetch_doctor_route():
    if (request.method == 'POST'):
        try:
            data = request.form
            code = data['code']
            # Call the main function in fetch_data.py
            # result = fetch_data.fetch_data(code, type="D")
            # result = fetch_data.fetch_doctor_data(username, password ,code)
            message1 = ''
            message2 = ''
            result1, result2 = fetch_data.fetch_doctor_data2(username, password ,code)
            if not result1 and not result2:
                message1 = f"There is no patients treated or examined by this doctor!"
            else:
                message1 = result1
                message2 = result2
                
            return render_template("fetch_doctor_data.html", message1=message1, message2=message2)

        except Exception as e:
            return render_template("fetch_doctor_data.html", message1=f'Error 1: {str(e)}', message2='')
    # For GET requests, simply render the page
    return render_template("fetch_doctor_data.html", message1='', message2 = '')

@app.route('/add_data', methods = ['GET', 'POST'])
def add_data_route():
    if (request.method == 'POST'):
        try:
            patient_data = request.form
            # Call the main function in add_patient.py
            result = add_patient.add_patient_2(username, password, patient_data)
            
            message = result
            return render_template("add_patient.html", message=message)
        except Exception as e:
            return render_template("add_patient.html", message=f"Error 2: {e}")
    # For GET requests, simply render the page
    return render_template("add_patient.html", message='')

@app.route('/fetch_payment', methods = ['GET', 'POST'])
def fetch_payment_route():
    if (request.method == 'POST'):
        try:
            code = request.form['code']
            type = request.form['patient_type']
            # Call the main function in add_patient.py
            # result = fetch_payment.fetch_payment(username, password, code)
            result1, result2 = fetch_payment.fetch_payment2(username, password, code, type)
                        
            if not result1:
                return render_template("fetch_payment.html", message1=f"There is no payment information for the patient {code}!", message2 = '', message3 = '')
            
            return render_template("fetch_payment.html", message1=result1, message2=result2, message3 = type)
        except Exception as e:
            return render_template("fetch_payment.html", message1=f'Error 2: {str(e)}', message2='', message3 = '')
    # For GET requests, simply render the page
    return render_template("fetch_payment.html", message1='', message2 = '', message3 = '' )
    
@app.route('/docLogin', methods = ['GET', 'POST'])
def doc_Login_route():
        if request.method == "POST":
            try:
                data = request.form
                global username
                global password
                username = data['username']
                password = data['password']
                db = mysql.connector.connect(user=username, password=password, host="localhost", database="hospital")

                cursor = db.cursor()

                # Execute a SELECT query to fetch the user's data
                query = "SELECT * FROM patient"
                cursor.execute(query)
                # Fetch the first row (if any)
                user_data = cursor.fetchall()

                # Check if a matching user was found
                if user_data:
                    return redirect(url_for('doc_homepage_route'))

            except Exception as e:
            # return render_template("login.html", message=f'Error: {str(e)}')
                return render_template("docLogin.html", message='Invalid username or password.')
        return render_template("docLogin.html", message='')

@app.route('/docHomepage', methods = ['GET', 'POST'])
def doc_homepage_route():
    return render_template("docHomepage.html")

@app.route('/docViewPatient', methods = ['GET', 'POST'])
def fetch_patient_route2():
    try:
        code = doctor_list[username]
        message1 = ''
        message2 = ''
        result1, result2 = fetch_data.fetch_doctor_data2(username, password ,code)
        if not result1 and not result2:
            message1 = f"There is no patients treated or examined by this doctor!"
        else:
            message1 = result1
            message2 = result2
            
        return render_template("docFetchPatient.html", message1=message1, message2=message2)

    except Exception as e:
        return render_template("docFetchPatient.html", message1=f'Error 1: {str(e)}', message2='')

if __name__ == '__main__':
    app.run(debug=True, port=5500)
