# 0x16. API advanced

This project includes Python scripts for interacting with the Reddit API. It covers various tasks involving API calls, parsing JSON data, and working with Reddit data.

## Dependencies

- Ubuntu 20.04 LTS 
- Python 3 (version 3.4.3)
- Requests library (for making HTTP requests to the Reddit API)

## Installations
```
pip install requests
```
## Project Tasks

| File Name      | Description |
| ---------------|-------------|
| `0-subs.py`    | Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. |
| `1-top_ten.py` | Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit. |
| `2-recurse.py` | Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. |
| `100-count.py` | Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords. |

## Usage

Each script can be executed individually by running `python script_name.py`, where `script_name.py` is the name of the Python script for the specific task.

For example:
```
python 0-subs.py programming
```
