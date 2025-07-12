import streamlit as st
from .snowflake_connector import get_connection
import pandas as pd
import plotly.express as px

def show_analytics():
    conn = get_connection()
    df = pd.read_sql("SELECT state, COUNT(*) as views FROM visits GROUP BY state", conn)
    fig = px.bar(df, x="state", y="views", title="Most Visited States")
    st.plotly_chart(fig)
