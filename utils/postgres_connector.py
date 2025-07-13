# utils/postgres_connector.py
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("PG_DB")
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT", 5432)

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def get_states():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT state_name FROM states_info")
    states = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return states

def get_state_info(state_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM states_info WHERE state_name = %s", (state_name,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return None
    return {
        "tagline": row[1],
        "image_url": row[2],
        "description": row[3],
        "places": row[4].split(','),
        "cuisine": row[5].split(','),
        "festivals": row[6].split(','),
        "language_snippets": eval(row[7])
    }

def log_visit(state):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits (state, timestamp) VALUES (%s, current_timestamp)", (state,))
    conn.commit()
    cur.close()
    conn.close()

def insert_review(state, email, review):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO reviews (state, email, review) VALUES (%s, %s, %s)", (state, email, review))
    conn.commit()
    cur.close()
    conn.close()

def fetch_reviews(state):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT email, review FROM reviews WHERE state = %s ORDER BY submitted_at DESC LIMIT 5", (state,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
