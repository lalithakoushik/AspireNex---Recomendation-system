import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\K LALITHA KOUSHIK\Desktop\aspirenex\task 2\Movie-Dataset-Latest.csv")
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['year'] = df['release_date'].dt.year
    return df

df = load_data()

# Title and description
st.title("Movie Ratings Analysis")
st.markdown("""
This app performs a simple analysis of a movie ratings dataset.
You can explore the distribution of votes, the popularity of movies, and the number of movies released over the years.
""")

# Sidebar for filtering
st.sidebar.header("Filter Options")
year_range = st.sidebar.slider("Select Year Range", int(df['year'].min()), int(df['year'].max()), (int(df['year'].min()), int(df['year'].max())))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Distribution of vote_average
st.subheader("Distribution of Vote Average")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_df['vote_average'], bins=30, kde=True, ax=ax)
ax.set_title('Distribution of Vote Average')
ax.set_xlabel('Vote Average')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Popularity vs Vote Average
st.subheader("Popularity vs Vote Average")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x='popularity', y='vote_average', ax=ax)
ax.set_title('Popularity vs Vote Average')
ax.set_xlabel('Popularity')
ax.set_ylabel('Vote Average')
st.pyplot(fig)

# Number of movies released each year
st.subheader("Number of Movies Released Each Year")
movies_per_year = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(15, 8))
sns.lineplot(x=movies_per_year.index, y=movies_per_year.values, ax=ax)
ax.set_title('Number of Movies Released Each Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Movies')
st.pyplot(fig)

# Top 10 most popular movies
st.subheader("Top 10 Most Popular Movies")
top_10_popular_movies = filtered_df.nlargest(10, 'popularity')[['title', 'popularity']]
st.table(top_10_popular_movies)

# Top 10 highest rated movies
st.subheader("Top 10 Highest Rated Movies")
top_10_rated_movies = filtered_df.nlargest(10, 'vote_average')[['title', 'vote_average']]
st.table(top_10_rated_movies)

# Run the Streamlit app
# To run this app, use the command: streamlit run app.py

