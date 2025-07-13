import streamlit as st
from .postgres_connector import insert_review, fetch_reviews

def review_form(state):
    with st.form(f"review_form_{state}"):
        email = st.text_input("Your Email")
        review = st.text_area("Your Review")
        submit = st.form_submit_button("Submit")
        if submit:
            insert_review(state, email, review)
            st.success("Review submitted!")

def display_reviews(state):
    rows = fetch_reviews(state)
    for r in rows:
        st.markdown(f"**{r[0]}**: {r[1]}")
