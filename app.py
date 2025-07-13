import streamlit as st
from utils.postgres_connector import get_states, get_state_info, log_visit, insert_review, fetch_reviews
from utils.ai_bot import get_bot_response
from utils.travel_planner import plan_trip
from utils.quiz import start_quiz
from utils.reviews import review_form, display_reviews
from utils.analytics import show_analytics
from utils.map_view import show_map
from utils.export_itinerary import export_pdf
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Incredible India Explorer", layout="wide")
st.title("Incredible India Explorer ❄️")
st.caption("Explore India. Powered by Snowflake.")

# Sidebar
states = get_states()
selected_state = st.sidebar.selectbox("Choose a State", states)
log_visit(selected_state)

# Main Content
state_info = get_state_info(selected_state)

st.header(f"{selected_state} – {state_info['tagline']}")
st.image(state_info["image_url"], width=600)
st.markdown(state_info["description"])
st.subheader("📍 Famous Places")
st.write(", ".join(state_info["places"]))
st.subheader("🍲 Cuisine")
st.write(", ".join(state_info["cuisine"]))
st.subheader("🎉 Festivals")
st.write(", ".join(state_info["festivals"]))
st.subheader("🗣️ Language")
for phrase in state_info["language_snippets"]:
    st.markdown(f"- **{phrase['en']}** → {phrase['native']}")

# Interactive Map
st.divider()
st.subheader("🗺️ Explore on Map")
show_map()

# AI Bot
st.divider()
st.subheader("🤖 Ask AI About Indian Culture")
q = st.text_input("Ask anything...")
if q:
    st.success(get_bot_response(q))

# Travel Planner
st.divider()
st.subheader("🧽 Plan Your Trip")
if st.button("Generate Itinerary"):
    plan = plan_trip("Your City", selected_state, "Culture")
    st.code(plan)
    export_pdf(plan, selected_state)

# Reviews
st.divider()
st.subheader("📝 Share Your Experience")
review_form(selected_state)
display_reviews(selected_state)

# Quiz
st.divider()
st.subheader("🧠 Quiz Time")
if st.button("Start Quiz"):
    start_quiz()

# Analytics
st.divider()
st.subheader("📊 Visitor Insights")
show_analytics()
