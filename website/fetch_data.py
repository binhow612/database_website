import mysql.connector

def fetch_data(username, password, code, type=None):
    # Establish the connection
    db = mysql.connector.connect(user=username, password= password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)

    try:
        if type == "P":
            # Fetch patient information from the 'patient' table
            cursor.execute("SELECT patient_type , Fname, Lname, phone_number FROM patient WHERE p_code = %s", (code,))

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
    
        elif type == "D":
            # Define the SQL query
            sql_query = """
                SELECT DISTINCT p.Code
                FROM patient p
                JOIN (
                    SELECT DISTINCT Outpat_code AS Code
                    FROM out_detail
                    WHERE Doc_code = %s
                    UNION
                    SELECT DISTINCT Inpat_code AS Code
                    FROM in_detail
                    WHERE Doc_code = %s
                ) t ON p.Code = t.Code;
            """

            # Execute the query
            cursor.execute(sql_query, (code, code))

            # Fetch the results
            results = cursor.fetchall()

            # Initialize an empty list to store the formatted messages
            messages = []

            # Display the results
            for result in results:
                code = result['Code']
                patient_data = fetch_data(code, "P")

                # Convert patient_data to a key-value pair string
                patient_str = ', '.join([f"{key}: {value}" for key, value in patient_data.items()])

                # Append the formatted patient string to the messages list
                messages.append(patient_str)

            # Combine the messages into a single string
            message = '\n'.join(messages)
            return message
        
    finally:
        # Close the connection
        cursor.close()
        db.close()

def fetch_patient_data(username, password, code, type):
    # Establish the connection
    db = mysql.connector.connect(user=username, password= password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)
    try:
        if (type=="OP"):
            cursor.execute("SELECT * FROM patient left join out_detail on patient.p_code = out_detail.outpat_code where p_code = %s and patient.patient_type = 'OP'", (code,))
        elif (type=="IP"):
            cursor.execute("select * from patient left join in_detail on patient.p_code = in_detail.inpat_code left join inpatient_record on patient.p_code = inpatient_record.in_code where p_code = %s and patient.patient_type = 'IP'", (code,))
        else:
            return "Error 2"
        patient_info = cursor.fetchall()
        if not patient_info:
            return "Error 1"
        return patient_info

    finally:
        # Close the connection
        cursor.close()
        db.close()

def fetch_doctor_data(username, password, code):
    # Establish the connection
    db = mysql.connector.connect(user=username, password= password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)
    try:

        sql_query = """
                SELECT *
                FROM patient p
                JOIN (
                    SELECT DISTINCT outpat_code AS Code
                    FROM out_detail
                    WHERE doc_code = %s
                    UNION
                    SELECT DISTINCT inpat_code AS Code
                    FROM in_detail
                    WHERE doc_code = %s
                ) t ON p.p_code = t.Code;
            """
        cursor.execute(sql_query, (code, code,))
        doctor_info = cursor.fetchall()
        if not doctor_info:
            return "Error 1"
        return doctor_info

    finally:
        # Close the connection
        cursor.close()
        db.close()
        pass

def fetch_doctor_data2(username, password, code):
    # Establish the connection
    db = mysql.connector.connect(user=username, password= password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)
    try:
        sql_query_in = """select * from patient 
                        join in_detail on patient.p_code = in_detail.inpat_code 
                        join inpatient_record on patient.p_code = inpatient_record.in_code
                        where doc_code= %s"""

        sql_query_out = """select * from patient 
                        join out_detail on patient.p_code = out_detail.outpat_code 
                        where doc_code= %s"""

        cursor.execute(sql_query_in, (code,))
        inpat_info = cursor.fetchall()

        cursor.execute(sql_query_out, (code,))
        outpat_info = cursor.fetchall()

        return inpat_info, outpat_info

    finally:
        # Close the connection
        cursor.close()
        db.close()
        pass