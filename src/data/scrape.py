from urllib import response

import pandas as pd
import requests as req

"""

scrape.py

Handles fetching and loading raw international match data.
Reads from the raw CSV source, filters from year 2000 onwards,
and drops irrelevant columns (city, country).

Output: cleaned DataFrame ready for export.py to process.

"""

# Step 1 - Define the URL of the raw CSV
MATCH_RESULTS_URL = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"

# Step 2 - Fetch the data using requests
def fetch_match_results(url=MATCH_RESULTS_URL):
    """Fetches the raw match results CSV data from the specified URL.
    
    Args:
        url (str): The URL to fetch the CSV data from. Defaults to MATCH_RESULTS_URL.
    
    Returns:
        str: The CSV data as a string.
    
    Raises:
        HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    response = req.get(url) # Fetch the CSV data from the URL
    response.raise_for_status()# Check for HTTP errors
    return response.text


# Step 3 - Load it into a pandas DataFrame

# Step 4 - Filter from year 2000 onwards

# Step 5 - Drop city and country columns

# Step 6 - Return the cleaned DataFrame