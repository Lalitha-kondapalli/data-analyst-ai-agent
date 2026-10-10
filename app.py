import streamlit as st
import pandas as pd
import plotly.express as px
from agent import agent

st.set_page_config(
    page_title="AI Data Analyst Agent",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analyst Agent")
st.write("Explore employee data and ask questions about salaries.")

@st.cache_data
def load_employee_data():
    return pd.read_csv("employees.csv")

try:
    data = load_employee_data()

    if data.empty:
        st.warning("The employee dataset is empty.")
        st.stop()

    required_columns = {"Employee", "Department", "Salary"}
    if not required_columns.issubset(data.columns):
        st.error("The CSV must contain Employee, Department, and Salary columns.")
        st.stop()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Employees", len(data))
    col2.metric("Average Salary", f"{data['Salary'].mean():,.2f}")
    col3.metric("Highest Salary", f"{data['Salary'].max():,.0f}")

    st.subheader("Employee Dataset")
    st.dataframe(data, use_container_width=True)

    st.subheader("Average Salary by Department")
    department_salary = (
        data.groupby("Department", as_index=False)["Salary"].mean()
    )

    chart = px.bar(
        department_salary,
        x="Department",
        y="Salary",
        title="Average Salary by Department",
        labels={"Salary": "Average Salary"}
    )
    st.plotly_chart(chart, use_container_width=True)

    st.subheader("Top-Paid Employees")
    top_employees = data.nlargest(5, "Salary")

    salary_chart = px.bar(
        top_employees,
        x="Employee",
        y="Salary",
        title="Top 5 Highest-Paid Employees",
        labels={"Salary": "Salary"}
    )
    st.plotly_chart(salary_chart, use_container_width=True)

    st.subheader("Ask Your Data Analyst Agent")
    question = st.text_input(
        "Enter a question",
        placeholder="Show the top 3 highest-paid employees"
    )

    if st.button("Analyze"):
        if question.strip():
            with st.spinner("Analyzing your question..."):
                result = agent(question, data)
            st.write("### Answer")
            st.write(result)
        else:
            st.warning("Please enter a question.")

except FileNotFoundError:
    st.error("employees.csv was not found. Keep it in the project folder.")
except Exception as error:
    st.error(f"Something went wrong: {error}")
