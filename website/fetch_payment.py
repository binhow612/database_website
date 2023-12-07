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

def fetch_payment2(username, password, code, type):
    # Establish the connection
    db = mysql.connector.connect(user=username, password=password, host="localhost", database="hospital")

    # Create a cursor object to interact with the database
    cursor = db.cursor(dictionary=True)

    try:
        query1 = '''select * from patient 
                        where p_code = %s'''
        # Execute the SQL query to fetch payment information
        if (type=="OP"):
            query2 = '''select 	
                        a.exami_no as examineNo,
                        a.exami_series_no as visit,
                        a.exami_time as treatTime,
                        a.exami_date as treatDate,
                        a.next_date as nextTreat,
                        a.fee as fee,
                        b.fname as docFname,
                        b.lname as docLname,
                        c.num_med as numMed,
                        d.med_name as medName,
                        d.price as medPrice,
                        c.num_med*d.price as cal_med_price
                from out_detail a
                join doctor b on a.doc_code = b.ecode
                join contain_out_detail c on a.outpat_code = c.outpat_code
                join medication d on c.med_code = d.med_code
                where a.outpat_code = %s
                order by a.exami_no'''
        elif (type=="IP"):
            query2 = '''select 	
                        d.fname as docFname,
                        d.lname as docLname,
                        b.record_no as visit,
                        b.admission_date as admitDate,
                        b.discharge_date as disDate,
                        b.fee as fee,
                        c.treatment_no as treatNo,
                        a.start_date as startDate,
                        a.end_date as endDate,
                        c.num_med as numMed,
                        e.med_name as medName,
                        e.price as medPrice,
                        c.num_med * e.price as cal_med_price
                from in_detail a
                join inpatient_record b on a.inpat_code = b.in_code
                join is_contained_in c on a.inpat_code = c.inpat_code
                join doctor d on a.doc_code = d.ecode
                join medication e on c.med_code = e.med_code
                where a.inpat_code = %s
                order by b.record_no''' 

        cursor.execute(query1, (code,))
        result1 = cursor.fetchall()

        cursor.execute(query2, (code,))
        result2 = cursor.fetchall()
        # Return the result
        return result1, result2

    except Exception as e:
        print(f"Error: {e}")
        return f"Error 1 : {e}", ""

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

    
