import streamlit as st

# Title of the dashboard
st.title("Smart Maintenance Dashboard")

# Current Date and Time
st.subheader("Current Date and Time")
current_time = "2026-02-26 16:06:31"
st.write(current_time)

# Example of an interactive widget
st.subheader("Select a Maintenance Task")
task = st.selectbox("Choose a task:", ["Task 1", "Task 2", "Task 3"])

if st.button('Submit'):
    st.write(f'You have selected: {task}')