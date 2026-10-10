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
        return data["Salary"].mean()
    if tool == "highest_salary":
        return data.loc[data["Salary"].idxmax()]
    if tool == "show_data":
        return data.head()
    return "I don't know how to answer that question yet."
def agent(question, data):
    tool = choose_tool(question, data)
    print("Selected tool:", tool)
    result = run_tool(tool, data)
    if isinstance(result, (int, float)) and pd.isna(result):
        return "Unable to calculate a valid result."
    return result
if __name__ == "__main__":
    df = load_data("employees.csv")
    question = input("Ask a question about the data: ")
    answer = agent(question, df)
    print("\nAnswer:")
    print(answer)
