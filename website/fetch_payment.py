import mysql.connector

def fetch_payment(username, password, code):
    # Establish the connection
    db = mysql.connector.connect(user=username, password=password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)

    try:
        # Execute the SQL query to fetch payment information
        query = '''
        SELECT DISTINCT
            p.p_code AS Patient_Code,
            p.patient_type AS Patient_Type,
            o.outpat_code AS Outpatient_Code,
            i.inpat_code AS Inpatient_Code,
            o.exami_no AS Treatment_No,
            o.treat_time AS Treatment_Time,
            o.treat_date AS Treatment_Date,
            o.next_date AS Next_Appointment_Date,
            o.fee AS Treatment_Fee,
            i.result AS Treatment_Result,
            i.start_date AS Treatment_Start_Date,
            i.end_date AS Treatment_End_Date,
            i.record_no AS Inpatient_Record_No,
            d.fname AS Doctor_FirstName,
            d.lname AS Doctor_LastName,
            d.specialty_name AS Doctor_Specialty,
            pr.provider_name AS Provider_Name,
            pr.address AS Provider_Address,
            pr.phone_number AS Provider_Phone,
            ip.provide_date AS Payment_Date,
            ip.price AS Payment_Price,
            o.diagnosis AS Outpatient_Diagnosis
        FROM
            patient p
        LEFT JOIN
            out_detail o ON p.p_code = o.outpat_code
        LEFT JOIN
            in_detail i ON p.p_code = i.inpat_code
        LEFT JOIN
            inpatient_record ir ON i.record_no = ir.record_no
        LEFT JOIN
            doctor d ON o.doc_code = d.ecode OR i.doc_code = d.ecode
        LEFT JOIN
            is_provided_by ip ON o.exami_no = ip.med_code OR i.treatment_no = ip.med_code
        LEFT JOIN
            provider pr ON ip.med_code = pr.provider_num
        WHERE
            p.p_code = %s
        '''

        cursor.execute(query, (code,))

        # Fetch all the results
        result = cursor.fetchall()

        # Return the result
        return result

    except Exception as e:
        print(f"Error: {e}")
        return f"Error 1 : {e}"

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

