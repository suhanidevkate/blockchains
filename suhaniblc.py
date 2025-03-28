import streamlit as st
import pandas as pd

# Initialize session state for the hospital ledger if not already present
if "hospital_ledger" not in st.session_state:
    st.session_state.hospital_ledger = {}

st.title("🏥 Hospital Ledger System")

# User input to add a patient visit
st.header("Add Patient Visit")
patient_name = st.text_input("Enter Patient's Name:")
treatment = st.text_input("Enter Treatment Received:")
cost = st.number_input("Enter Cost of Treatment ($):", min_value=0.0, format="%.2f")
date_of_visit = st.date_input("Enter Date of Visit")

if st.button("Add Visit"):
    if patient_name and treatment and cost:
        visit = {"treatment": treatment, "cost": cost, "date_of_visit": str(date_of_visit)}
        if patient_name not in st.session_state.hospital_ledger:
            st.session_state.hospital_ledger[patient_name] = []
        st.session_state.hospital_ledger[patient_name].append(visit)
        st.success(f"Visit added for {patient_name} on {date_of_visit}.")
    else:
        st.warning("Please fill in all fields.")

# Display the hospital ledger
st.header("📋 Hospital Ledger Records")
if st.session_state.hospital_ledger:
    for patient, visits in st.session_state.hospital_ledger.items():
        st.subheader(f"Patient: {patient}")
        df = pd.DataFrame(visits)
        st.dataframe(df)
else:
    st.write("No records found. Add a visit above.")
