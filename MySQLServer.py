import mysql.connector
from mysql.connector import Error

def create_database():
    conn = None
    try:
        # ---------------------------------------
        # CONNECT TO MYSQL SERVER
        # ---------------------------------------
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="201305Thami,,,"  # <-- change to your MySQL root password
        )

        if conn.is_connected():
            mycursor = conn.cursor()

            # ---------------------------------------
            # CREATE DATABASE (NO SELECT / NO SHOW)
            # ---------------------------------------
            mycursor.executemycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("Error connecting to MySQL server:", e)

    finally:
        # ---------------------------------------
        # CLOSE CONNECTION
        # ---------------------------------------
        if conn is not None and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

# Run the function
create_database()
