from tiniworld_core.logic.data import Tiniworld
import pandas as pd
import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
from webapp.methods import AppFunktion

from tiniworld_core.logic.params import LOCAL_DATA_PATH
# webpage 01 - Tiniworld locations
# -----------------------------
# This page is used to explore the diferent Tiniworld locations on a map

st.set_page_config(page_title="Tiniworld locations", page_icon="🌍", layout="wide",initial_sidebar_state = "expanded")

# instanciating Tiniworld class
tini = Tiniworld()
AF = AppFunktion()
AF.load_session_state()

with st.sidebar:
    AF.sidebar()

def show_line_plot(df):
    # plot example graph
    df_con_3 = df
    fig_3 = px.line(df_con_3, x='docDate', y='qty',
                  color="store_code",
                  line_group="store_code", hover_name="store_code")
    fig_3.update_layout(title='Footfall, locations' , showlegend=True)
    return fig_3

# Header
tiniworldLocations = st.container()
with tiniworldLocations:
    col1, col2, col3 = st.columns([6,1,1])
    with col1:
        '''### Tiniworld locations'''
    with col2:
        st.write("")
    with col3:
        st.image(
            "https://theme.hstatic.net/200000113805/1000623432/14/image_partner2.png",
            width=80,
        )

# Text
'''
There are 62 Tiniworlds located in Vietnam. We want to select one and look at it´s data. \n
⬅️ please choose one location from the sidebar.
'''

# Map
location_file = f"{LOCAL_DATA_PATH}/tw_location_info.csv" #Load OK
df_locations = pd.read_csv(location_file)[['latitude', 'longitude']]
st.map(df_locations)
