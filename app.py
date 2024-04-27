import pickle
import pandas as pd
import streamlit as st
import numpy as np


st.header("Books Recommendation System ")
model = pickle.load(open('artifacts/model.pkl', 'rb')) 
books = pickle.load(open('artifacts/books.pkl', 'rb')) 
book_with_tags = pickle.load(open('artifacts/book_with_tags.pkl', 'rb')) 
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))



def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

def fetch_posterContent(suggestion):
    book_name = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(books[book_id]['title'])
        url = books[book_id]['image_url']
        poster_url.append(url)
    return poster_url


# def recommend_book(book_name):
#     books_list = []
#     book_id = np.where(book_pivot.index == book_name)[0][0]
#     distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=11 )

#     poster_url = fetch_poster(suggestion)
    
#     for i in range(len(suggestion)):
#             books = book_pivot.index[suggestion[i]]
#             for j in books:
#                 books_list.append(j)
#     return books_list , poster_url    
   
def search_books_by_title(title):
    # Filter book_with_tags for rows where the title matches
    matching_books = book_with_tags[book_with_tags['title'].str.lower() == title.lower()]

    if matching_books.empty:
        return "No books found with the given title."

    # Drop duplicates based on title and goodreads_book_id
    matching_books = matching_books.drop_duplicates(subset=['title', 'goodreads_book_id'])

    # Select relevant columns for output
    result = matching_books[['title', 'author', 'year', 'average_rating', 'tag_name', 'image_url']]
    
    return result



def recommend_book(book_name):
    book_row = book_pivot.loc[book_name]
    
    # Reshape the row for model prediction
    book_row = book_row.values.reshape(1, -1)
    
    # Get nearest neighbors
    distances, indices = model.kneighbors(book_row, n_neighbors=20)
    
    recommendations = pd.DataFrame(columns=['title', 'author', 'year', 'average_rating', 'tag_name', 'image_url'])
    recommended_books = set()  # Use a set to keep track of recommended books to avoid duplicates

    for i in range(len(indices[0])):
        book_details = search_books_by_title(book_pivot.index[indices[0][i]])
        recommended_books.add(book_details.iloc[0]['title'])  # Add book title to set
        recommendations = recommendations.append(book_details)

    # Drop duplicates based on title
    recommendations = recommendations.drop_duplicates(subset=['title'])

    return recommendations




# def recommend_book(book_name):
#     # Get the row corresponding to the provided book_name
#     book_row = book_pivot.loc[book_name]
    
#     # Reshape the row for model prediction
#     book_row = book_row.values.reshape(1, -1)
    
#     # Get nearest neighbors
#     distances, indices = model.kneighbors(book_row, n_neighbors=20)
    
#     recommendations = []
#     for i in range(len(indices[0])):
#         book_details = {
#             'title': book_pivot.index[indices[0][i]],
#             'rating': distances[0][i]

#         }
#         recommendations.append(book_details)
        
#     return recommendations


  
# #searching books by there title 
# def search_books_by_title(keyword):
#     books_list = []
#     matching_book_ids = np.where(book_pivot.index.str.contains(keyword, case=False))
#     # print(matching_book_ids)
#     poster_url = fetch_poster(matching_book_ids)
    
#     for i in range(len(matching_book_ids)):
#             books = book_pivot.index[matching_book_ids[i]]
#             for j in books:
#                 books_list.append(j)
     
#     return books_list , poster_url 

#### to be worked upon
def search_books(keyword):
    matching_books = book_with_tags[book_with_tags.apply(lambda row: keyword.lower() in row['title'].lower() or 
                                                                   keyword.lower() in ' '.join(row['tag_name']).lower() or
                                                                   keyword.lower() in row['author'].lower() or
                                                                   keyword.lower() in str(row['year']), axis=1)]
    matching_books = matching_books.sort_values(by='average_rating', ascending=False)
    result = matching_books[['title', 'author', 'image_url', 'average_rating', 'tag_name', 'year']].reset_index(drop=True)
    return result



# Page 2: About Page
# Page 1: Home Page
def home_page():
    st.title("Home Page")
    st.write("<p style='font-size:20px;'>Welcome to our Project!</p>", unsafe_allow_html=True)
    st.write("<p style='font-size:20px;'>This is a Book Recommendation System, designed to help you choose your next book to read.</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size:18px;'>Recommendation systems are becoming increasingly important in today’s busy world. "
                "People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. "
                "Therefore, recommendation systems are crucial as they help them make the right choices, "
                "without having to expend their cognitive resources.</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size:18px;'>The purpose of a recommendation system is to search for content that would be interesting to an individual. "
                "It involves a number of factors to create personalized lists of useful and interesting content specific to each user/individual. "
                "Recommendation systems are Artificial Intelligence-based algorithms that analyze all possible options and create a customized list of items "
                "that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, "
                "what other people with similar traits/demographics are watching, and how likely you are to engage with those books. "
                "This is achieved through predictive modeling and heuristics with the data available.</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 '>In this Project we developed two models for suggesting good books to our users.</h3>", unsafe_allow_html=True)
    st.markdown("<h4 '>1. Content Based Filtering</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px;'>The first model is developed using the content based filtering. In this model we used the content like book's title, its author, the genre to search the book.</p>", unsafe_allow_html=True)
    
    st.markdown("<h4 '>2. Item Based Collaborative  Filtering</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px;'>The Second model is developed using the collaborative filtering. In this model we used the dataset from kaggle and then cleaned it and preprocessed it to get a clean and clear dataset for our model to improve accuracy."
                "In this method we used dataset of books that contains books details like bookname,isbn, author,category, publisher etc. and a user dataset for user details, and ratings dataset that contains ratings provided by user to this books"
                "We applied item based collaborative filtering so that we can recommend books similar to the book that is currently selected by the user</p>", unsafe_allow_html=True)
    
    # col1, col2 = st.columns(2)
    # with col1:
    #     if st.button("Content-Based Filtering", key='content_button_home'):
    #         # st.experimental_set_query_params(selected_page="Content Based Filtering")
    #         pass

    # with col2:
    #     if st.button("Collaborative Filtering", key='collab_button_home'):
    #         # st.experimental_set_query_params(selected_page="Collaborative Filtering")
    #         pass
# Sidebar Navigation

def contentFiltering_page():

    st.title("Content Based Filtering")
    st.markdown("Content-based systems use characteristic information and take item attributes into consideration. Examples include Twitter and YouTube. These systems consider what content you are interacting with (e.g., what music you are listening to, what singer you are watching) to form embeddings for the features.")
    st.markdown("User-specific actions or similar items are recommended. It will create a vector of it. These systems make recommendations using a user's item and profile features. They hypothesize that if a user was interested in an item in the past, they will once again be interested in it in the future.")
    st.markdown("Advantages of Content-Based Filtering:")
    st.markdown("- Does not rely on user behavior or historical data.")
    st.markdown("- Can recommend niche or less-popular items.")
    st.markdown("- Provides explanations for recommendations based on item attributes.")
    st.markdown("- Can handle new users effectively.")
    st.markdown("- Can make recommendations even when there are few or no user interactions.")
    st.markdown("One issue that arises is making obvious recommendations because of excessive specialization (e.g., user A is only interested in categories B, C, and D, and the system is not able to recommend items outside those categories, even though they could be interesting to them).")

    search_this_books = st.text_input("Type a book name, genre, author, publisher : Content based filtering")

    if st.button('Search'):
        if search_books:
            matching_books = search_books(search_this_books)
            st.write("Books matching the keyword:")
            num_rows = len(matching_books)
            if(num_rows<1):
                st.text("No Matching books were found")
                
            if num_rows>30:
                num_rows = 30
            num_cols = 5
            num_rows_per_col = num_rows // num_cols
            if num_rows_per_col<1:
                col1, col2, col3, col4, col5 = st.columns(5)
                for j in range(num_rows):
                    with locals()[f'col{j+1}']:
                        st.text(matching_books.iloc[j]['title'])
                        st.image(matching_books.iloc[j]['image_url'])
            else:
                for i in range(num_rows_per_col):
                    col1, col2, col3, col4, col5 = st.columns(5)
                    for j in range(num_cols):
                        idx = i * num_cols + j
                        if idx < num_rows:
                            with locals()[f'col{j+1}']:
                                st.text(matching_books.iloc[idx]['title'])
                                st.image(matching_books.iloc[idx]['image_url'])



# Page 3: Contact Page
def CollaborativeFiltering_page():
    st.title("Item based Collaborative")
    st.markdown("Collaborative filtering systems, which are based on user-item interactions.")
    st.markdown("Clusters of users with same ratings, similar users.")
    st.markdown("Book recommendation, so use cluster mechanism.")
    st.markdown("We take only one parameter, ratings or comments.")
    st.markdown("In short, collaborative filtering systems are based on the assumption that if a user likes item A and another user likes the same item A as well as another item, item B, the first user could also be interested in the second item.")
    st.markdown("Advantages of Collaborative Filtering:")
    st.markdown("- Learns user preferences without requiring detailed item attributes.")
    st.markdown("- Can be effective even for new items without much historical data.")
    st.markdown("- Does not rely on content features or domain-specific knowledge.")
    st.markdown("- Can capture evolving user preferences and trends.")
    st.markdown("- Can provide serendipitous recommendations based on user behavior.")
    st.markdown("- Can handle a large number of items and users.")
    st.markdown("Issues are:")
    st.markdown("- User-Item nXn matrix, so computationally expensive.")
    st.markdown("- Only famous items will get recommended.")
    st.markdown("- New items might not get recommended at all.")

    selected_books = st.selectbox(
    "Type or select a book from the dropdown for Collaborative Filtering",
    book_with_tags['title'])


    if st.button('Show Recommendation(Collaborative Filtering)'):
        recommended_books = recommend_book(selected_books)

        num_rows = len(recommended_books)

        num_cols = 5
        num_rows_per_col = num_rows // num_cols
        for i in range(num_rows_per_col):
            col1, col2, col3, col4, col5 = st.columns(5)
            for j in range(num_cols):
                idx = i * num_cols + j
                if idx < num_rows:
                    with locals()[f'col{j+1}']:
                        st.text(recommended_books.iloc[idx]['title'])
                        st.image(recommended_books.iloc[idx]['image_url'])

    



# url_params = st.experimental_get_query_params()
# selected_page_btn = url_params.get('selected_page', ['Home'])[0]

# Sidebar Navigation
selected_page = st.sidebar.radio("Navigation", ["Home", "Content Based Filtering", "Collaborative Filtering"])

if selected_page == "Home":
    home_page()
elif selected_page == "Content Based Filtering":
    contentFiltering_page()
elif selected_page == "Collaborative Filtering":
    CollaborativeFiltering_page()


