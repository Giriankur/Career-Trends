import streamlit as st
import pandas as pd

# Define the recommend_jobs function
def recommend_jobs(user_preferences, top_n=5):
    # Mock logic for recommendation (replace this with your actual model logic)
    recommendations = pd.DataFrame({
        'title': ['Data Scientist', 'Machine Learning Engineer', 'Data Analyst', 'Software Developer', 'AI Engineer'],
        'category': ['IT', 'IT', 'IT', 'Software', 'AI'],
        'hourly_low': [0.5, 0.6, 0.4, 0.7, 0.8],
        'hourly_high': [0.8, 0.9, 0.7, 0.85, 0.95],
        'similarity_score': [0.95, 0.92, 0.87, 0.85, 0.83]
    })
    return recommendations.head(top_n)

# Streamlit UI
st.title("Job Recommendation System")
st.sidebar.header("Input Your Preferences")

# Collect user inputs
hourly_low = st.sidebar.slider("Minimum Hourly Rate", 0.0, 1.0, 0.5)
hourly_high = st.sidebar.slider("Maximum Hourly Rate", 0.0, 1.0, 0.7)
budget = st.sidebar.slider("Budget", 0.0, 1.0, 0.6)
job_title = st.sidebar.text_input("Preferred Job Title", "data scientist")
category = st.sidebar.text_input("Job Category", "IT")
job_recency = st.sidebar.slider("Job Recency (days)", 0, 365, 30)

user_preferences = {
    'hourly_low': hourly_low,
    'hourly_high': hourly_high,
    'budget': budget,
    'job_title': job_title,
    'category': category,
    'job_recency': job_recency
}

# Recommend jobs
if st.sidebar.button("Get Recommendations"):
    try:
        recommendations = recommend_jobs(user_preferences)
        st.write("### Recommended Jobs")
        st.dataframe(recommendations[['title', 'category', 'hourly_low', 'hourly_high', 'similarity_score']])
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
