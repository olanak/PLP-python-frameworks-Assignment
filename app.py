# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("./data/cord19_cleaned.csv")  #   cleaned file
    return df

df = load_data()

# -----------------------------
# App Layout
# -----------------------------
st.title("📊 CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research metadata")

# Show sample of data
if st.checkbox("Show raw data sample"):
    st.write(df.head(20))

# -----------------------------
# Interactive Widgets
# -----------------------------
# Year Range Selector
min_year = int(df['year'].min(skipna=True))
max_year = int(df['year'].max(skipna=True))

year_range = st.slider("Select year range", min_year, max_year, (2015, 2020))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Source Filter
sources = df['source'].dropna().unique().tolist()
selected_source = st.selectbox("Select a source (optional)", ["All"] + sources)

if selected_source != "All":
    filtered_df = filtered_df[filtered_df['source'] == selected_source]

st.write(f"Filtered dataset shape: {filtered_df.shape}")

# -----------------------------
# Visualizations
# -----------------------------
# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue", ax=ax)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(y=top_journals.index, x=top_journals.values, color="lightgreen", ax=ax)
ax.set_title("Top 10 Journals")
ax.set_xlabel("Count")
st.pyplot(fig)

# Word Cloud of Titles
st.subheader("Word Cloud of Paper Titles")
text_titles = " ".join(filtered_df['title'].dropna().astype(str).tolist())

wordcloud = WordCloud(
    width=800, height=400,
    background_color="white",
    colormap="viridis",
    max_words=100
).generate(text_titles)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Source Distribution
st.subheader("Top Sources")
top_sources = filtered_df['source'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(y=top_sources.index, x=top_sources.values, color="steelblue", ax=ax)
ax.set_title("Top 10 Sources")
st.pyplot(fig)
