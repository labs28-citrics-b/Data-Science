import os
import psycopg2

def fetch_query_records(query, params=None):
    """ Creates a connection to database; returns query from specified table.
    Input: query (a SQL query string)
    Returns: response (cursor.fetchall() obj in array form)
    """
    
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PW = os.environ['DB_PW']
    DB_HOST = os.environ['DB_HOST']

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

