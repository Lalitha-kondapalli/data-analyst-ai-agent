
# Data Analyst AI Agent

## Overview
A beginner-friendly Python project that analyzes employee data from a CSV file and selects an analysis tool based on a user's question.

## Features
- Load employee data using Pandas.
- Calculate average salary.
- Find the highest salary.
- Compare average salaries by department.
- Display sample employee records.
- Select an analysis tool based on predefined question patterns.

## Technologies
- Python
- Pandas
- CSV data

## Project Files
- `agent.py` - Main program and tool-selection logic.
- `employees.csv` - Sample employee dataset.
- `requirements.txt` - Required Python library.

## Installation
Install Python, then run:

```bash
pip install -r requirements.txt
```

## Run the Project
Run this command in the project folder:

```bash
python agent.py
```

Ask a question such as:

`Which department has the highest average salary?`

## Current Limitations
This is an early, rule-based prototype. It does not yet use an LLM, persistent memory, or an autonomous reasoning loop.

## Future Improvements
- Integrate an LLM.
- Add more analysis tools.
- Validate outputs and handle errors.
- Create automated tests to evaluate correctness.
