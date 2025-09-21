import streamlit as st
import pandas as pd

# ---------- Queue Data ----------
if 'queue' not in st.session_state:
    st.session_state.queue = []

if 'current_token' not in st.session_state:
    st.session_state.current_token = 0

# ---------- Functions ----------
def add_person(roll, name, branch, year, purpose):
    st.session_state.current_token += 1
    student_info = {
        "Token": st.session_state.current_token,
        "Roll No": roll,
        "Name": name,
        "Branch": branch,
        "Year": year,
        "Purpose": purpose
    }
    st.session_state.queue.append(student_info)
    st.success(f"Token assigned successfully! Your Token Number: {st.session_state.current_token}")

def serve_next():
    if st.session_state.queue:
        student = st.session_state.queue.pop(0)
        st.success(f"Serving Token: {student['Token']} - {student['Name']} ({student['Purpose']})")
    else:
        st.info("No students in the queue!")

def cancel_token(token):
    original_len = len(st.session_state.queue)
    st.session_state.queue = [s for s in st.session_state.queue if s['Token'] != token]
    if len(st.session_state.queue) < original_len:
        st.success(f"Token {token} has been cancelled!")
    else:
        st.warning(f"No student found with Token {token}.")

# ---------- Streamlit UI ----------
st.title("SmartQ Management System - MRECW Admin Block")
st.markdown("*Malla Reddy Engineering College for Women - Admin Queue*")

# ---------- 1️⃣ Register ----------
st.header("1️⃣ Register for Your Token")
with st.form("student_form"):
    roll_no = st.text_input("Enter Your Roll Number")
    name = st.text_input("Enter Your Name")
    branch = st.selectbox("Select Your Branch", ["EEE", "ECE", "CSE", "AIML", "IOT", "OTHER"])
    year = st.selectbox("Select Your Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    purpose = st.selectbox(
        "Purpose of Visit",
        ["College Fee", "Bus Fee", "Certificate Submission", "Income Tax Certificate", "Other"]
    )
    submit = st.form_submit_button("Get Token")
    
    if submit:
        if roll_no and name:
            add_person(roll_no, name, branch, year, purpose)
        else:
            st.warning("Please fill in both Roll Number and Name.")

# ---------- 2️⃣ Current Queue ----------
st.header("2️⃣ Current Queue")
if st.session_state.queue:
    for idx, student in enumerate(st.session_state.queue):
        if idx == 0:
            st.markdown(f"➡ Token {student['Token']}: {student['Name']} | Roll: {student['Roll No']} | "
                        f"Branch: {student['Branch']} | Year: {student['Year']} | Purpose: {student['Purpose']}")
        else:
            st.write(f"Token {student['Token']}: {student['Name']} | Roll: {student['Roll No']} | "
                     f"Branch: {student['Branch']} | Year: {student['Year']} | Purpose: {student['Purpose']}")
else:
    st.write("Queue is empty.")

# ---------- 3️⃣ Serve Next ----------
st.header("3️⃣ Serve Next Student")
if st.button("Serve Next"):
    serve_next()

# ---------- 4️⃣ Cancel Token ----------
st.header("4️⃣ Cancel a Token")
token_to_cancel = st.number_input("Enter Token Number to Cancel", min_value=1, step=1)
if st.button("Cancel Token"):
    cancel_token(token_to_cancel)

# ---------- 5️⃣ Next Few Students----------
st.header("5️⃣ Next Few Students in Line")

next_students = st.session_state.queue[:5]
if next_students:
    for student in next_students:
        st.markdown(f"*Token {student['Token']}: {student['Name']} ({student['Purpose']})*")
else:
    st.write("No one waiting in the queue.")
