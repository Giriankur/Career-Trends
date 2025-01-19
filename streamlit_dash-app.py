import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    df = pd.read_csv('updated_data.csv')
    df['published_date'] = pd.to_datetime(df['published_date'])
    df['year_month'] = df['published_date'].dt.to_period('M')
    return df

df = load_data()

# Sidebar for user input
st.sidebar.header("Job Market Insights")
metric = st.sidebar.selectbox("Choose a Metric to Analyze", ['Roles', 'Salaries', 'Categories'])

# Dashboard title
st.title("Dynamic Job Market Trends")

if metric == 'Roles':
    st.header("Top In-Demand Roles")
    role_counts = df['title'].value_counts().head(10)
    st.bar_chart(role_counts)

elif metric == 'Salaries':
    st.header("Salary Trends Over Time")
    salary_trends = df.groupby('year_month')['budget'].mean()
    st.line_chart(salary_trends)

elif metric == 'Categories':
    st.header("Most Popular Job Categories")
    category_counts = df['category'].value_counts().head(10)
    st.bar_chart(category_counts)

# Display raw data (optional)
if st.checkbox("Show Raw Data"):
    st.dataframe(df)
