"""
export.py

Handles saving and loading processed match and team statistics data to and from CSV files.

Saves cleaned DataFrame to data/processed/results_clean.csv

and loads it back for use by stats.py, predictor.py, and app.py.

Output: data/processed/results_clean.csv

"""

from src.data.scrape import clean_match_results
import pandas as pd
import os


PROCESSED_PATH = "data/processed/results_clean.csv"
TEAM_STATS_PATH = "data/processed/team_stats.csv"


def save_match_results(df, path=PROCESSED_PATH):
    """Saves the processed DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        path (str): The file path to save the CSV. Defaults to PROCESSED_PATH.
    
    Returns:
        None
    """
    folder = os.path.dirname(path) # Get the directory from the path

    os.makedirs(folder, exist_ok=True) # Ensure the directory exists

    df.to_csv(path, index=False) # Save the DataFrame to CSV without the index
    
    print(f"Processed match results saved to {path}") # Confirmation message


def load_processed_match_results(path=PROCESSED_PATH):
    """Loads the processed match results from a CSV file.
    
    Args:
        path (str): The file path to load the CSV from. Defaults to PROCESSED_PATH.
    
    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed results file not found at {path}. Please run the data processing pipeline first.")
    
    df = pd.read_csv(path) # Load the processed results from CSV
    return df # Return the loaded DataFrame


def save_team_stats(df, path=TEAM_STATS_PATH):
    """Saves the team statistics DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The team statistics DataFrame to save.
        path (str): The file path to save the CSV. Defaults to TEAM_STATS_PATH.
    
    Returns:
        None
    """

    #Getting the directory from the team stats path
    folder = os.path.dirname(path)

    #Ensure the directory exists before saving the team stats CSV
    os.makedirs(folder , exist_ok=True)


    # Save the team stats DataFrame to CSV without the index
    df.to_csv(path, index=False)

    print(f"Team statistics saved to {path}") # Confirmation message



def load_team_stats(path=TEAM_STATS_PATH):
    """Loads the team statistics from a CSV file.
    
    Args:
        path (str): The file path to load the CSV from. Defaults to TEAM_STATS_PATH.
    
    Returns:
        pd.DataFrame: The loaded team statistics DataFrame.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Team statistics file not found at {path}. Please run the team stats calculation pipeline first.")
    
    df = pd.read_csv(path) # Load the team statistics from CSV
    return df # Return the loaded team statistics DataFrame


    


if __name__ == "__main__":
    from src.data.scrape import clean_match_results
    print("Processing match results...")

    df = clean_match_results() # Get the cleaned match results DataFrame

    save_match_results(df) # Save the cleaned DataFrame to CSV
    print("Data processing complete.")

    df_load = load_processed_match_results() # Load the processed match results back from CSV
    print("Loaded processed match results:")

    print(df_load.head()) # Print the first few rows of the loaded DataFrame to confirm it worked
    print(f"Total matches: {len(df_load)}") # Print the total number of matches in the loaded DataFrame
