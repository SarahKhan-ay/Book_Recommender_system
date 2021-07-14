import pickle
import streamlit as st

def recommend(book):
    index = books[books['title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    image_url_list = []
    author_list = []
    publication_year = []
    rating = []
    for i in distances[1:6]:
        author_list.append(books.iloc[i[0]].authors)
        publication_year.append(books.iloc[i[0]].publication_year)
        rating.append(books.iloc[i[0]].average_rating)
        image_url_list.append(books.iloc[i[0]].image_url)
        recommended_book_names.append(books.iloc[i[0]].title)

    return recommended_book_names, image_url_list, author_list, publication_year, rating

st.header('Book Recommender System')
books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity (1).pkl', 'rb'))

book_list = books['title'].values
selected_book = st.selectbox(
    "Type or select a book",
    book_list
)

if st.button('Show Recommendation'):
    recommended_book_names, image_url_list, author_list, publication_year, rating = recommend(selected_book)
    for i in range(5):
        col1, col2 = st.beta_columns(2)
        with col1:
            st.image(image_url_list[i], width=190)
        with col2:
            st.subheader(recommended_book_names[i])
            st.markdown('Written By', unsafe_allow_html=False)
            st.text(author_list[i])
            st.markdown('Publication Year', unsafe_allow_html=False)
            st.text(publication_year[i])
            st.markdown('Rating', unsafe_allow_html=False)
            st.text(rating[i])
