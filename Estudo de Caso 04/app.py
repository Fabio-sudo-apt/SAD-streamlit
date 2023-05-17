import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url_google = "https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/edit#gid=1378939680"

def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

st.set_page_config(page_title="Dashboard - SISREF")

st.sidebar.title("Configurações de Exibição")

data = load_data(url_google)

df = pd.DataFrame(data)

fig, ax = plt.subplots()

colors = ['green']

ax.hist(df["Refeicao"], bins=10, color=colors)

st.pyplot(fig)