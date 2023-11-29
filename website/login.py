import mysql.connector
import hashlib

#-----------------------------------------------------------LOGIN------------------------------------------------------------#
def login(username, password):
    db = None
    cursor = None
    try:
        # Establish the connection
        db = mysql.connector.connect(user="root", password="1234", host="localhost", database="User_Account")

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Execute a SELECT query to fetch the user's data
        query = "SELECT * FROM user_account WHERE username = %s AND password = %s"
        cursor.execute(query, (username, hashed_password))

        # Fetch the first row (if any)
        user_data = cursor.fetchall()

        # Check if a matching user was found
        if user_data:
            return "Successful"
        else:
            return "Invalid username or password."
            
    finally:
        # Close the cursor and connection
        if (cursor):
            cursor.close()
        if (db):
            db.close()

#-----------------------------------------------REGISTER--------------------------------------------------------------#
def create_database_if_not_exists():
    connection = mysql.connector.connect(user="root", password="1234", host="localhost")
    cursor = connection.cursor()

    # Create the database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS User_Account")
    cursor.execute("USE User_Account")

    # Create the 'users' table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_account (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(64) NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()

def register(username, password, email):
    # Create the database if not exist
    create_database_if_not_exists()

    # Establish the connection
    connection = mysql.connector.connect(user="root", password="1234", host="localhost", database="User_Account")
    cursor = connection.cursor()

    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Insert user data into the 'user_account' table
        cursor.execute("INSERT INTO user_account (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
        connection.commit()
        return "Successful"
    except mysql.connector.Error as e:
        return f"Error 1: {str(e)}"
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

#---------------------------------------------------------------MAIN-----------------------------------------------#
def main(option, username, password, email=None):
    if (option == "R"):
        # Perform registration
        return register(username, password, email)

    elif (option == "L"):
        # Perform login
        return login(username, password)