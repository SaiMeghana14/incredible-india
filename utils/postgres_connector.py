# utils/postgres_connector.py
import psycopg2
import os
import json
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

DB_NAME = os.getenv("PG_DB")
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT", 5432)

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    try:
        yield conn
    finally:
        conn.close()

def get_states():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT DISTINCT state_name FROM states_info")
            return [row[0] for row in cur.fetchall()]

def get_state_info(state_name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM states_info WHERE state_name = %s", (state_name,))
            row = cur.fetchone()
    if not row:
        return None
    return {
        "tagline": row[1],
        "image_url": row[2],
        "description": row[3],
        "places": row[4].split(','),
        "cuisine": row[5].split(','),
        "festivals": row[6].split(','),
        "language_snippets": json.loads(row[7])
    }

def log_visit(state):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO visits (state, timestamp) VALUES (%s, current_timestamp)", (state,))
            conn.commit()

def insert_review(state, email, review):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO reviews (state, email, review) VALUES (%s, %s, %s)", (state, email, review))
            conn.commit()

def fetch_reviews(state):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT email, review FROM reviews WHERE state = %s ORDER BY submitted_at DESC LIMIT 5", (state,))
            return cur.fetchall()
