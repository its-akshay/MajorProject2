# Major Project 2: Book Recommendation System

### Acropolis Institute of Technology and Research

## Contributors

| Name               | Github-ID                                      |
| ------------------ | ---------------------------------------------- |
| Akshay Keswani     | [@its-akshay](https://www.github.com/its-akshay) |
| Akshat Singh Gour  | [@akshat123007](https://github.com/akshat123007) |
| Akshat Singh Rathore | [@AkshatSR2003](https://github.com/AkshatSR2003) |
| Aayush Gupta       | [@AayushGuptaP1](https://github.com/AayushGuptaP1) |

# Project Coordinator:
#### - Prof. Juhi Shrivastava

## Tech Stack

**Client:** Python, Colab (for testing and data preprocessing)  
**Frontend:** HTML, CSS, JavaScript & Streamlit



## Images

![2](https://github.com/its-akshay/MajorProject2/assets/71098450/81c8deb7-64c9-4fc0-90ad-0507da8fe5cb)  
![1](https://github.com/its-akshay/MajorProject2/assets/71098450/699660b7-de9b-4b8f-a0aa-ab728417010d)  
![3](https://github.com/its-akshay/MajorProject2/assets/71098450/444b136b-304e-4852-a53a-4740118fea20)



# Project: Book Recommender System Using Machine Learning! | Collaborative Filtering Based

In today’s fast-paced world, recommendation systems play a crucial role in helping individuals make informed choices amidst their busy schedules. These systems leverage artificial intelligence algorithms to curate personalized lists of relevant content tailored to each user's preferences, based on factors like their profile, browsing history, and similarities with other users.

## Types of Recommendation Systems:

### 1) Content Based:

Content-based systems consider item attributes and characteristic information to make recommendations. Examples include Twitter and YouTube, where recommendations are made based on what users are currently engaging with, such as music or videos. These systems create vectors for item features and recommend similar items or user-specific actions.

One challenge with content-based systems is their tendency to make obvious recommendations due to excessive specialization, limiting recommendations to specific categories even when broader options may be of interest.

### 2) Collaborative Filtering:

Collaborative filtering systems rely on user-item interactions to make recommendations. By identifying clusters of users with similar preferences or behaviors, these systems can recommend items based on the preferences of similar users. However, they face challenges such as computational complexity, bias towards famous items, and difficulty recommending new items.

## About this Project:

This project is a Streamlit web application that recommends various books based on user interests.

## Dataset Used:

* [Dataset link](https://www.kaggle.com/ra4u12/bookrecommendation)

## Concept Used to Build the Model (model.pkl):

1. Load the dataset.
2. Initialize the value of k.
3. Iterate through the training data points to predict the class.
4. Calculate the Euclidean distance between the test data and each training data point.
5. Sort the distances in ascending order.
6. Retrieve the top k rows from the sorted array.

## How to Run?

### Steps:

1. Clone the repository.

2. Create a conda environment after opening the repository:
conda create -n books python=3.7.10 -y

3. activate the environment
conda activate books

4. Installing the requirements
pip install -r requirements.txt

5. Run the following file to generate the models:
Books Recommender.ipynb

6. Finally, run the Streamlit app:
streamlit run app.py




