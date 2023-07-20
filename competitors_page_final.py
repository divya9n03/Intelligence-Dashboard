import streamlit as st
import pandas as pd
import webbrowser
import io
import requests

NEWS_API_KEY = "f534874620a94f80a14772f28ac93d77"
st.set_page_config(layout="wide")


def fetch_articles(prompt):

    url = f"https://newsapi.org/v2/everything?q={prompt}&pageSize=2&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    # print(data)
    articles = data["articles"]
    return articles


st.header('Bayer')
if st.button("PowerBI"):
    url = "https://www.google.com"  # Replace this URL with your desired destination
    webbrowser.open_new_tab(url)

st.markdown('---')
# Create two columns with full-width using the custom CSS class
col1, col2 = st.columns(2)
col1.markdown("<div class='full-width'>", unsafe_allow_html=True)
col2.markdown("<div class='full-width'>", unsafe_allow_html=True)


def fetch_csv_from_github(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Read CSV data using pandas
            csv_data = pd.read_csv(io.StringIO(response.text))
            print(csv_data)
            # st.write(csv_data)
            return csv_data
        else:
            print(
                f"Error: Unable to fetch CSV file. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# Add elements to the first column, first row
with col1.container():
    st.header("Data from annual report")

    github_raw_url = "https://github.com/divya9n03/Intelligence-Dashboard/blob/e86f0c4b09537711ec1ee4b0a5cb891b2f65d2a2/EN2022_07_Five-Year-Summary.csv?raw=true"
    csv_data = fetch_csv_from_github(github_raw_url)
    st.dataframe(csv_data)


with col2.container():
    st.header('Competitor Research')
    articles = fetch_articles(
        'OTCPharm OR Pharma OR Stada OR Sanofi OR Servier OR Abbott OR Noavrtis OR Teva OR KRKA OR Glaxosmithkline')

    if st.button("Get more"):
        articles = fetch_articles(
            'OTCPharm OR Pharma OR Stada OR Sanofi OR Servier OR Abbott OR Noavrtis OR Teva OR KRKA OR Glaxosmithkline')
        # Display the news articles
        for article in articles:
            st.subheader(article['publishedAt'])
            st.subheader(article["title"])
            st.write(article["description"])
            st.write(article["url"])
            st.write(article['source']['name'])
            st.markdown("---")


st.markdown("---")
# Create two more columns
col3 = st.columns(1)

with st.container():
    st.header('Clinical trial updates')
    articles = fetch_articles(
        'clinical trial OR pharma OR medicine OR drugs OR Pharma')

    if st.button("Refresh news"):
        articles = fetch_articles(
            'clinical trial OR pharma OR medicine OR drugs OR Pharma')
        # Display the news articles
        for article in articles:
            st.subheader(article['publishedAt'])
            st.subheader(article["title"])
            st.write(article["description"])
            st.write(article["url"])
            st.write(article['source']['name'])
            st.markdown("---")
