
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def choose_tool(question, data):
    question = question.lower()

    if "highest average salary" in question:
        return "highest_average_salary"

    if "average salary" in question or "mean salary" in question:
        return "average_salary"

    if "highest salary" in question or "maximum salary" in question:
        return "highest_salary"

    if "lowest salary" in question or "minimum salary" in question:
        return "lowest_salary"

    if "count employees" in question or "how many employees" in question:
        return "count_employees"

    if "show data" in question or "display data" in question:
        return "show_data"

    return "unknown"

def run_tool(tool, data):
    if "Salary" not in data.columns:
        return "Error: Salary column not found."

    if tool == "highest_average_salary":
        result = data.groupby("Department")["Salary"].mean()
        return result.sort_values(ascending=False).head(1)

    if tool == "average_salary":
        return f"The average salary is {data['Salary'].mean():.2f}."

    if tool == "highest_salary":
        employee = data.loc[data["Salary"].idxmax()]
        return f"The highest-paid employee is {employee['Employee']} with a salary of {employee['Salary']}."

    if tool == "lowest_salary":
        employee = data.loc[data["Salary"].idxmin()]
        return f"The lowest-paid employee is {employee['Employee']} with a salary of {employee['Salary']}."

    if tool == "count_employees":
        if "Department" not in data.columns:
            return "Error: Department column not found."
        return data["Department"].value_counts()

    if tool == "show_data":
        return data.head()

    return "I don't know how to answer that question yet."

def agent(question, data):
    tool = choose_tool(question, data)
    print("Selected tool:", tool)
    return run_tool(tool, data)

if __name__ == "__main__":
    df = load_data("employees.csv")
    question = input("Ask a question about the data: ")
    answer = agent(question, df)

    print("\nAnswer:")
    print(answer)
