import streamlit as st
import pandas as pd

# Title of the app
st.title("🧮 Interactive Insurance Premium Calculator")

# Sidebar for user input
st.sidebar.header("Enter Your Details")

# User Inputs
age = st.sidebar.slider('Age', 18, 100, 30)
gender = st.sidebar.selectbox('Gender', ['Male', 'Female', 'Other'])
smoker = st.sidebar.radio('Smoking Status', ['Yes', 'No'])
coverage = st.sidebar.number_input('Coverage Amount ($)', value=100000)

# Function to calculate premium
def calculate_premium(age, gender, smoker, coverage):
    base_rate = 0.0005  # Base rate per dollar of coverage
    age_factor = 1 + (age - 30) * 0.01
    smoker_factor = 1.5 if smoker == 'Yes' else 1
    gender_factor = 0.95 if gender == 'Female' else 1

    premium = coverage * base_rate * age_factor * smoker_factor * gender_factor
    return premium

# Calculate premium based on inputs
premium = calculate_premium(age, gender, smoker, coverage)

# Display the result
st.subheader("🔢 Your Estimated Annual Premium:")
st.success(f"${premium:,.2f}")

# Generate a graph: Premium vs Age
st.subheader("📈 How Premium Changes with Age")

# Create data for the plot
ages = list(range(18, 101))
premiums = [calculate_premium(a, gender, smoker, coverage) for a in ages]

# Create DataFrame
df = pd.DataFrame({
    'Age': ages,
    'Premium': premiums
})

# Plot using Streamlit's built-in chart
st.line_chart(df.set_index('Age'))

# Fun Tip
st.info("💡 Tip: Buying insurance when you're young and healthy saves you a lot of money over time!")
