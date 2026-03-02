import streamlit as st # Web application easy code  
import pandas as pd #
import os # System menage our project ke error understande ?
import json   # Project ke data ko save karta ha 

FILE = "students.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load (file)
    return []

def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)

# ADD_STUDENT

def Add_Student(Name,Father,Phone,Email,Roll):
    data = load_data()

    # check duplicate roll
    for s in data:
        if s["Roll"] == Roll:
            return False, " Roll Number Already Exists!"

    student = {
        "Name": Name,
        "Father": Father,
        "Phone": Phone,
        "Email": Email,
        "Roll": Roll
    }
    data.append(student)
    save_data(data)
    return True, "✔ Student added successfully!"

#STUDENT VIEW

def student_view():
    return load_data()

#Update  Function use for the basic python code 

def update_student(Name,Father,Phone,Email,Roll):
     data = load_data()
     for  student in data:
         if student["Name"] == Name:
             student["Father"] == Father
             student["Phone"] == Phone
             student["Email"] == Email
             student["ROll"] ==Roll
             save_data(data)
             return True,"Student Update Successfully!"
     return False,"! Stydent Not Found!"

#  SEARCH STUDENT python basic code 
def Search_Student_ID(roll):
    data = load_data()
    for s in data:
        if s["Roll"] == roll:
            return s
    return None

# DELETE STUDENT Python basic code
def delete_student(roll):
    data = load_data()
    new_data = [s for s in data if s["Roll"] != roll]
    if len(new_data) != len(data):
        save_data(new_data)
        return True, "✔ Student Deleted Successfully!"
    return False, " Roll number not found!"


 # streamlit 

st.set_page_config(page_title="Student Management System", layout="centered")
st.title("Student Management System")

menu = st.sidebar.selectbox("Select option",
            ["Add Student","View Student","Search Student_ID","Updates Student Record","Delete Student"])

# ADD STUDENT
if menu == "Add Student":
    st.header("Add Student")

    Name = st.text_input("Student Name")
    Father = st.text_input("Father Name")
    Phone = st.text_input("Phone Number")
    Email = st.text_input("Email")
    Roll = st.text_input("Roll Number")

    if st.button("Add Student"):
        if not Name or not Father or not Phone or not Email or not Roll:
            st.error("All fields are required.")
        else:
            ok, msg = Add_Student(Name, Father, Phone, Email, Roll)
            st.success(msg) if ok else st.error(msg)

# VIEW STUDENT
elif menu == "View Student":
    st.header(" All Students")
    data = load_data()
    if data:
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("No student data found.")

# SEARCH STUDENT

elif menu == "Search Student_ID":
    st.subheader(" Search by Student Roll Number")
    
    roll = st.text_input("Enter Student Roll Number")
     # Search button 
    if st.button("Search"):
        result = Search_Student_ID(roll)

        if result:
            st.success(f"Student record found for: {roll}")
            st.json(result)
        else:
            st.warning(" No student found with this roll number.")


# UPDATE STUDENT

elif menu == "Update Student":
    st.subheader(" Update student")
    roll =st.text_input(" Student Update Recorde")
    
    if st.button("Recorde"):
        Student = Search_Student_ID(roll)
        if not Student:
            st.error("Not Found")
        else:
            st.write("Leave field empty if you don’t want to modify.")

            Name = st.text_input("Student Name",value=Student['Name'])
            Father = st.text_input("Father Name",value=Student["Father"])
            Phone = st.text_input("Phone Number",value=Student["Phone"])
            Email = st.text_input("Email",value=Student['Email'])
            Roll = st.text_input("Roll Number",value=Student["Roll"])

            if st.button("Update Now"):
                ok,msg = update_student(Name,Father,Phone,Email,Roll)
                st.success(msg)if ok else st.error(msg)                                  

#DELET FUNCTION

elif menu =="Delet":
    st.subheader("Delet Student Record")
    roll =st.text_input(" Enter Roll to Delet")
    if st.button("Delet"): 
        ok, msg= delete_student(roll)
        st.success(msg) if ok else st.error(msg)


