import streamlit as st

def start_quiz():
    questions = [
        {"q": "Which state is known as the Land of Five Rivers?", "a": "Punjab"},
        {"q": "Where is the Sun Temple located?", "a": "Konark"},
        {"q": "Which dance form originated in Kerala?", "a": "Kathakali"}
    ]
    score = 0
    for i, q in enumerate(questions):
        answer = st.text_input(f"Q{i+1}: {q['q']}", key=f"quiz_{i}")
        if answer.lower() == q['a'].lower():
            score += 1
    st.success(f"Your Score: {score}/{len(questions)}")
