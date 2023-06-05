import streamlit as st
import pandas as pd
import numpy as npv

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

dt = pd.read_csv("songs.csv")

df = pd.DataFrame(dt)

st.table(dt)