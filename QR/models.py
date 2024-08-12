import mysql.connector
from mysql.connector import errorcode

DATABASE_CONFIG = {
    'user': 'root',
    'password': 'Jhazenne31!',
    'host': '127.0.0.1',
    'port': 3307,
    'database': 'qr_code_db'
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DATABASE_CONFIG)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qrcode_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL,
            encrypted_content TEXT NOT NULL,
            pin VARCHAR(255) NOT NULL,
            file_path VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

create_table()
