# 0x15. API

This project includes Python script that retrieves task data from the JSONPlaceholder API for all employees and exports the data in JSON format. The generated JSON file is named "todo_all_employees.json.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Tasks](#tasks)


## Description

The JSONPlaceholder Data Exporter is a Python script that fetches data from the JSONPlaceholder API. It retrieves tasks associated with users and organizes them into a JSON file.

## Requirements

- Python 3.x
- Requests library (install using `pip install requests`)

## Usage

1. Ensure you have Python 3.x installed on your system.

2. Install the required Requests library by running the following command:

   ```bash
   pip install requests
   ```

3. Run the script using the following command:

   ```bash
   python 3-dictionary_of_list_of_dictionaries.py
   ```

   This will execute the script, retrieve task data for all employees, and create the "todo_all_employees.json" file.

## Project Tasks

| File Name                       | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| 0-gather_data_from_an_API.py    | Python script to fetch employee data from a web API and export it in JSON format. |
| 1-export_to_CSV.py              | Python script to convert the JSON data into a CSV file with a specific format. |
| 2-export_to_JSON.py             | Python script to export a user's tasks in JSON format. |
| 3-dictionary_of_list_of_dictionaries.py | Python script to export JSON data of tasks for all employees. |

