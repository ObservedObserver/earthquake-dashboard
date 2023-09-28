import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html

st.set_page_config(
    page_title="Earthquake Visualization with pygwalker",
    layout="wide"
)

st.title("Earthquake Visualization (1900-2023) with pygwalker")

# Initialize pygwalker communication
init_streamlit_comm()

# When using `use_kernel_calc=True`, you should cache your pygwalker html, if you don't want your memory to explode
@st.cache_resource
def get_pyg_html(df: pd.DataFrame) -> str:
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    html = get_streamlit_html(df, use_kernel_calc=True, spec="./spec/geo_vis.json", debug=False)
    return html

@st.cache_data
def get_df() -> pd.DataFrame:
    return pd.read_csv("./Significant Earthquake_Dataset_1900_2023.csv")

df = get_df()

components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)