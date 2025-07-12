import snowflake.connector
import os

def get_connection():
    return snowflake.connector.connect(
        user=os.getenv("SF_USER"),
        password=os.getenv("SF_PASSWORD"),
        account=os.getenv("SF_ACCOUNT"),
        warehouse=os.getenv("SF_WAREHOUSE"),
        database=os.getenv("SF_DATABASE"),
        schema=os.getenv("SF_SCHEMA")
    )

def get_states():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT state_name FROM states_info")
    return [row[0] for row in cur.fetchall()]

def get_state_info(state_name):
    conn = get_connection()
    cur = conn.cursor()
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
        "language_snippets": eval(row[7])
    }

def log_visit(state):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits (state, timestamp) VALUES (%s, current_timestamp())", (state,))
    conn.commit()
