import mysql.connector

def add_patient(username, password, patient_data):
    # Establish the connection
    db = mysql.connector.connect(user=username, password=password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    try:
        # Insert patient information into the 'patient' table
        cursor.execute(
            "INSERT INTO patient (Code, Patient_type, Fname, Lname, DOB, Gender, Address, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (patient_data['code'], patient_data['patientType'], patient_data['fname'],
             patient_data['lname'], patient_data['DOB'], patient_data['gender'], patient_data['address'],
             patient_data['phoneNumber'])
        )
        
        # Insert additional details based on patient type
        if patient_data['patientType'] == 'IP':
            cursor.execute(
                "INSERT INTO in_detail (Inpat_code, Doc_code, Treatment_no, Record_no, Start_date, End_date, Result) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (patient_data['code'], patient_data['docCode'], patient_data['treatmentNo'], patient_data['recordNo'],
                 patient_data['startDate'], patient_data['endDate'], patient_data['result'])
            )
        elif patient_data['patientType'] == 'OP':
            cursor.execute(
                "INSERT INTO out_detail (Outpat_code, Doc_code, Treatment_no, time, Date, Next_date, Fee, Diagnosis) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (patient_data['code'], patient_data['docCode'], patient_data['treatmentNo'],
                 patient_data['time'], patient_data['date'], patient_data['nextDate'],
                 patient_data['fee'], patient_data['diagnosis'])
            )
        # Commit the changes
        db.commit()
        return f"Patient with code {patient_data['code']} added successfully!"
    
    except Exception as e:
        return f"Error 1: {e}"
    
    finally:
        # Close the connection
        cursor.close()
        db.close()

def add_patient_2(username, password, patient_data):
        # Establish the connection
    db = mysql.connector.connect(user=username, password=password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    try:
        # Insert patient information into the 'patient' table
        cursor.execute(
            "insert into patient (patient_type, fname, lname, dob, gender, address, phone_number) values (%s, %s, %s, %s, %s, %s, %s)",
            (patient_data['patientType'], patient_data['fname'],
             patient_data['lname'], patient_data['DOB'], patient_data['gender'], patient_data['address'],
             patient_data['phoneNumber'])
        )
        db.commit()
        return "Added successfully!"
    except Exception as e:
        return f"Error 1: {e}"
    
    finally:
        # Close the connection
        cursor.close()
        db.close()
        pass