from flask import Flask, jsonify
import pymysql
import os
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

def get_db_connection():
    """Establish a connection to the database."""
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection

@app.route('/')
def index():
    """Test database connection and show the name of the connected database."""
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
    connection.close()
    
    return jsonify({'connected_to': result[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
