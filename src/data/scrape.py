from urllib import response

import pandas as pd
import requests as req
from io import StringIO

"""

scrape.py

Handles fetching and loading raw international match data.
Reads from the raw CSV source, filters from year 2000 onwards,
and drops irrelevant columns (city, country).

Output: cleaned DataFrame ready for export.py to process.

"""

# Define the URL of the raw CSV
MATCH_RESULTS_URL = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"

# Fetch the data using requests
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
    
    return response.text #input for def load_match_results


# Load into a pandas DataFrame
def load_match_results(csv_data):
    """Loads the CSV data into a pandas DataFrame.
    
    Args:
        csv_data (str): The CSV data as a string.
    
    Returns:
        pd.DataFrame: The loaded DataFrame.

    df : DataFrame

    StringIO : Converts the CSV string data into a file like object that can be read by pandas.
    """
    
    df = pd.read_csv(StringIO(csv_data)) # Load the CSV data into a DataFrame
    return df

# Filter from year 2000 onwards
def filter_match_results_by_year(df):
    """Filters the DataFrame to include only matches from year 2000 onwards.
    
    Args:
        df (pd.DataFrame): The DataFrame to filter.
    
    Returns:
        pd.DataFrame: The filtered DataFrame with matches from year 2000 onwards.
        
        matches_2000_onwards : new DataFrame
    """
    df['date'] = pd.to_datetime(df['date']) # Convert the 'date' column to datetime
    matches_2000_onwards = df[df['date'].dt.year >= 2000] # Filter matches from year 2000 onwards
    return matches_2000_onwards

# Drop city and country columns
def drop_city_country_columns(df):
    """Drops the 'city' and 'country' columns from the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to modify.
    
    Returns:
        pd.DataFrame: The DataFrame with the 'city' and 'country' columns dropped.
        
        dropped_city_country : new DataFrame
    """

    dropped_city_country = df.drop(columns=["city", "country"]) # Drop the 'city' and 'country' columns
    return dropped_city_country


# Return the cleaned DataFrame
def clean_match_results():
    
    """Cleans the match results DataFrame by fetching raw data, filtering by year, and dropping irrelevant columns.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    
    """


    csv_data = fetch_match_results() # Fetch the raw CSV data
    df = load_match_results(csv_data) # Load the CSV data into a DataFrame
    filtered_df = filter_match_results_by_year(df) # Filter matches from year 2000 onwards
    cleaned_df = drop_city_country_columns(filtered_df) # Drop the 'city' and 'country' columns
    
    return cleaned_df # Return the cleaned DataFrame