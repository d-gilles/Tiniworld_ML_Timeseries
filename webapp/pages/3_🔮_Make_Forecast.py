from tiniworld_core.logic.data import Tiniworld
from webapp.methods import AppFunktion
import streamlit as st
# webpage 03 - Forecast
# -----------------------------
# This page is used to forecast the footfall for a location

st.set_page_config(page_title=f"Forecast", page_icon="🔮", layout="wide",initial_sidebar_state = "expanded")

# instanceating Tiniworld class
tini = Tiniworld()
AF = AppFunktion()

with st.sidebar:
    AF.sidebar()

modelPrediction = st.container()

with modelPrediction:
# header
    col1, col2, col3 = st.columns([4,3,1])
    with col1:
        '''### Forecast on footfall for a location'''
    with col2:
        f'''
        Store name: {st.session_state.store_name} \n
        Store nr: {st.session_state['store']} '''
    with col3:
        st.image(
            "https://theme.hstatic.net/200000113805/1000623432/14/image_partner2.png",
            width=80,
        )
# forecast
    period_to_forecast = 300
    fig_fc = tini.plot_forecast(st.session_state.store, period_to_forecast)

    fig_fc.update_layout(width=1000)
    st.write(fig_fc)
