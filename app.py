import streamlit as st
from utils.snowflake_connector import get_states, get_state_info
from utils.ai_bot import get_bot_response
from utils.travel_planner import plan_trip
from utils.quiz import start_quiz

st.set_page_config(page_title="Incredible India Explorer", layout="wide")
st.title("🇮🇳 Incredible India Explorer")
st.caption("Powered by Snowflake ❄️")

# State list from Snowflake
states = get_states()
selected_state = st.sidebar.selectbox("Choose a State/UT", states)

# Fetch data for selected state
state_info = get_state_info(selected_state)

st.header(f"{selected_state} – {state_info['tagline']}")
st.image(state_info["image_url"], width=600)
st.markdown(state_info["description"])

st.subheader("📍 Famous Places")
st.write(", ".join(state_info["places"]))

st.subheader("🍲 Local Cuisine")
st.write(", ".join(state_info["cuisine"]))

st.subheader("🎉 Festivals")
st.write(", ".join(state_info["festivals"]))

st.subheader("🗣️ Learn Local Language")
for phrase in state_info["language_snippets"]:
    st.markdown(f"- **{phrase['en']}** → {phrase['native']}")

# AI Chatbot
st.divider()
st.subheader("🤖 Ask Incredible India AI")
query = st.text_input("Ask me about Indian states or culture...")
if query:
    st.success(get_bot_response(query))

# Travel Planner
st.divider()
st.subheader("🧭 Travel Planner")
if st.button("Plan a trip"):
    st.info(plan_trip("Your City", selected_state, "Culture"))

# Quiz
st.divider()
st.subheader("🧠 Quiz Time!")
if st.button("Start Quiz"):
    start_quiz()
