import unittest
import pandas as pd
from agent import choose_tool, run_tool

class TestDataAnalystAgent(unittest.TestCase):

    def setUp(self):
        self.data = pd.read_csv("employees.csv")

    def test_lowest_salary_tool(self):
        tool = choose_tool("Who has the lowest salary?", self.data)
        self.assertEqual(tool, "lowest_salary")

    def test_highest_salary_tool(self):
        tool = choose_tool("What is the highest salary?", self.data)
        self.assertEqual(tool, "highest_salary")

    def test_average_salary(self):
        result = run_tool("average_salary", self.data)
        expected = self.data["Salary"].mean()
        actual = float(result.split()[-1].rstrip("."))
        self.assertAlmostEqual(actual, expected, places=2)

    def test_department_employee_count(self):
        result = run_tool("count_employees", self.data)
        self.assertEqual(result.sum(), len(self.data))

    def test_top_paid_employees_tool(self):
        tool = choose_tool("Show the top 3 highest-paid employees", self.data)
        self.assertEqual(tool, "top_paid_employees")

    def test_top_paid_employees_result(self):
        result = run_tool(
            "top_paid_employees",
            self.data,
            "Show the top 3 highest-paid employees"
        )
        self.assertEqual(len(result), min(3, len(self.data)))
        self.assertTrue(result["Salary"].is_monotonic_decreasing)

if __name__ == "__main__":
    unittest.main()
