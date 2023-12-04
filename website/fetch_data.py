import mysql.connector

def fetch_data(code, type=None):
    # Establish the connection
    db = mysql.connector.connect(user="root", password="1234", host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)

    try:
        if type == "P":
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
