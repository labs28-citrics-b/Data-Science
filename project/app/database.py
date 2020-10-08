import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def fetch_query_records(query, params=None):
    """ Creates a connection to database; returns query from specified table.
    Input: query (a SQL query string)
    Returns: response (cursor.fetchall() obj in array form)
    """
    
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PW = os.getenv("DB_PW")
    DB_HOST = os.getenv("DB_HOST")

    conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PW,
            host=DB_HOST)

    cursor = conn.cursor()

    cursor.execute(query, params)

    response = cursor.fetchall()

    conn.close()

    return response

