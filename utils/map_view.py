import streamlit as st
import folium
from streamlit_folium import st_folium

def show_map():
    m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)
    folium.Marker([26.9124, 75.7873], tooltip="Jaipur").add_to(m)
    folium.Marker([10.8505, 76.2711], tooltip="Kerala").add_to(m)
    st_folium(m, width=700)
