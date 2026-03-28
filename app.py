import streamlit as st
import pandas as pd

st.title("Fast Food Protein per Dollar")

st.write("Prototype dashboard to find cheapest protein from major chains.")

data = [
    {"restaurant": "McDonald's", "item": "McDouble", "protein_g": 22, "price_usd": 2.79},
    {"restaurant": "Taco Bell", "item": "Bean Burrito", "protein_g": 13, "price_usd": 1.99},
]
df = pd.DataFrame(data)
df["protein_per_dollar"] = df["protein_g"] / df["price_usd"]

st.dataframe(df.sort_values("protein_per_dollar", ascending=False))
