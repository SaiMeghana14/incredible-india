import streamlit as st
from .snowflake_connector import get_connection

def review_form(state):
    with st.form(f"review_form_{state}"):
        email = st.text_input("Your Email")
        review = st.text_area("Your Review")
        submit = st.form_submit_button("Submit")
        if submit:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO reviews (state, email, review) VALUES (%s, %s, %s)", (state, email, review))
            conn.commit()
            st.success("Review submitted!")

def display_reviews(state):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT email, review FROM reviews WHERE state = %s ORDER BY submitted_at DESC LIMIT 5", (state,))
    rows = cur.fetchall()
    for r in rows:
        st.markdown(f"**{r[0]}**: {r[1]}")
