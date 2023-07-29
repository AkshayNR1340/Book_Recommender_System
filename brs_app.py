import numpy as np
import pickle
import streamlit as st

st.header('Book Recommender System')
model = pickle.load(open('BRSmodel.pkl','rb'))
book_names = pickle.load(open('book_names.pkl','rb'))
finaldf = pickle.load(open('finaldf1.pkl','rb'))
pivot = pickle.load(open('pivot.pkl','rb'))


def fetch_poster(suggestion):
    book_name = []
    imgs_index = []
    book_url = []

    for book_id in suggestion:
        book_name.append(pivot.index[book_id])

    for name in book_name[0]:
        imgs = np.where(finaldf['Book-Title'] == name)[0][0]
        imgs_index.append(imgs)

    for idx in imgs_index:
        url = finaldf.iloc[idx]['Image-URL-M']
        book_url.append(url)

    return book_url


def recommend_book(book_name):
    books_list = []
    book_id = np.where(pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=7)

    book_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list, book_url



selected_books = st.selectbox(
    "Search your book", book_names
)



if st.button('Give Recommendation'):
    recommended_books, book_url = recommend_book(selected_books)
    column1, column2, column3, column4, column5, column6 = st.columns(6)
    with column1:
  
        st.markdown(recommended_books[1])
        st.image(book_url[1])

    with column2:
       
        st.markdown(recommended_books[2])
        st.image(book_url[2])

    with column3:
        
        st.markdown(recommended_books[3])
        st.image(book_url[3])

    with column4:
       
        st.markdown(recommended_books[4])
        st.image(book_url[4])

    with column5:
        
        st.markdown(recommended_books[5])
        st.image(book_url[5])

    with column6:
        
        st.markdown(recommended_books[6])
        st.image(book_url[6])