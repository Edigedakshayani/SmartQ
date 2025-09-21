import streamlit as st

# ---------- Queue Data ----------
if 'queue' not in st.session_state:
    st.session_state.queue = []  # Store all student details

if 'current_token' not in st.session_state:
    st.session_state.current_token = 0  # Last assigned token

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

# ---------- Streamlit UI ----------
st.title("SmartQ Management System - MRECW Admin Block")
st.markdown("**Malla Reddy Engineering College for Women - Admin Block Queue**")

st.header("1️⃣ Register for Your Token")
with st.form("student_form"):
    roll_no = st.text_input("Enter Your Roll Number")
    name = st.text_input("Enter Your Name")
    branch = st.selectbox("Select Your Branch", ["EEE", "ECE", "CSE", "AIML", "IOT", "OTHER"])
    year = st.selectbox("Select Your Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    purpose = st.selectbox("Purpose of Visit", [
        "College Fee",
        "Bus Fee",
        "Certificate Submission",
        "Income Tax Certificate",
        "Other"
    ])
    submit = st.form_submit_button("Get Token")
    
    if submit:
        if roll_no and name:
            add_person(roll_no, name, branch, year, purpose)
        else:
            st.warning("Please fill in both Roll Number and Name.")

st.header("2️⃣ Current Queue")
if st.session_state.queue:
    for student in st.session_state.queue:
        st.write(f"Token {student['Token']}: {student['Name']} | Roll: {student['Roll No']} | "
                 f"Branch: {student['Branch']} | Year: {student['Year']} | Purpose: {student['Purpose']}")
else:
    st.write("Queue is empty.")

st.header("3️⃣ Serve Next Student")
if st.button("Serve Next"):
    serve_next()

st.header("4️⃣ Next Few Students in Line")
next_students = st.session_state.queue[:5]
if next_students:
    for student in next_students:
        st.write(f"Token {student['Token']}: {student['Name']} ({student['Purpose']})")
else:
    st.write("No one waiting in the queue.")
