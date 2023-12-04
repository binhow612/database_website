import mysql.connector
from datetime import datetime

def fetch_data(code):
    # Establish the connection
    db = mysql.connector.connect(user="root", password="1234", host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)

    try:
        # Fetch patient information from the 'patient' table
        cursor.execute("SELECT * FROM patient WHERE Code = %s", (code,))

        patient_info = cursor.fetchone()
        
        if not patient_info:
            return "Error 1"

        patient_type = patient_info['patient_type']

        # Fetch additional details based on the patient type
        if patient_type == "IP":
            cursor.execute("SELECT * FROM in_detail WHERE Inpat_code = %s", (code,))
            additional_info = cursor.fetchone()
        elif patient_type == "OP":
            cursor.execute("SELECT * FROM out_detail WHERE Outpat_code = %s", (code,))
            additional_info = cursor.fetchone()
        else:
            return "Error 2"

        # Combine patient information with additional details
        result = {**patient_info, **additional_info} if additional_info else patient_info
        return result

    finally:
        # Close the connection
        cursor.close()
        db.close()