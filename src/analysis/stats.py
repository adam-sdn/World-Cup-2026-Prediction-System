"""

stats.py

Handles saving and loading processed match data.
Loads the cleaned DataFrame from export.py and provides functions to compute statistics like win/loss ratios, average goals, and performance trends.
Defines constants for statistical analysis, such as tournament weightings.


"""


import pandas as pd
from data.export import load_processed_match_results


# Constants for stats.py
STATS_FROM_2014 = 2014


# Tournament weightings for statistical analysis
OURNAMENT_WEIGHINGS = {
    "FIFA World Cup": 3,
    "UEFA Euro": 3,
    "Copa América": 3,
    "Africa Cup of Nations": 3,
    "FIFA World Cup qualification": 2,
    "UEFA Euro qualification": 2,
    "UEFA Nations League": 2,
    "Friendly": 1
}

# List of countries that have qualified for the FIFA World Cup 2026
WC_2026_COUNTRIES = [
    # Group A
    "Mexico", "South Africa", "South Korea", "Czech Republic",
    # Group B
    "Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland",
    # Group C
    "Brazil", "Morocco", "Haiti", "Scotland",
    # Group D
    "United States", "Paraguay", "Australia", "Turkey",
    # Group E
    "Germany", "Curaçao", "Ivory Coast", "Ecuador",
    # Group F
    "Netherlands", "Japan", "Sweden", "Tunisia",
    # Group G
    "Belgium", "Egypt", "Iran", "New Zealand",
    # Group H
    "Spain", "Cape Verde", "Saudi Arabia", "Uruguay",
    # Group I
    "France", "Senegal", "Iraq", "Norway",
    # Group J
    "Argentina", "Algeria", "Austria", "Jordan",
    # Group K
    "Portugal", "DR Congo", "Uzbekistan", "Colombia",
    # Group L
    "England", "Croatia", "Ghana", "Panama"
]


def get_team_matches(df, team):
    """Returns a DataFrame of matches involving the specified team.
    
    Args:
        df (pd.DataFrame): The DataFrame containing match data.
        team (str): The name of the team to filter by.
    
    Returns:
        pd.DataFrame: A DataFrame of matches involving the specified team.
    """
    team_matches = df[(df["home_team"] == team) | (df["away_team"] == team)] # Filter matches where the team is either home or away
    return team_matches # Return the filtered DataFrame



def filter_by_year(df):
    """Filters the DataFrame to include only matches from year 2014 onwards.
    
    Args:
        df (pd.DataFrame): The DataFrame to filter.
    
    Returns:
        pd.DataFrame: The filtered DataFrame with matches from year 2014 onwards.
    """
    df['date'] = pd.to_datetime(df['date']) # Convert the 'date' column to datetime

    filtered_df = df[df['date'].dt.year >=  STATS_FROM_2014] # Filter matches from year 2014 onwards
    return filtered_df # Return the filtered DataFrame


def assign_tournament_weight(df):
    """Assigns a weight to each match based on the tournament type.
    
    Args:
        df (pd.DataFrame): The DataFrame containing match data.

    Returns:
        pd.DataFrame: The DataFrame with a new 'tournament_weight' column.
    """
    weight_category_3 = df[(df['tournament'] == "FIFA World Cup") | (df['tournament'] == "UEFA Euro") | (df['tournament'] == "Copa América") | (df['tournament'] == "Africa Cup of Nations")] # Define category 3 tournaments
    weight_category_2 = df[(df['tournament'] == "FIFA World Cup qualification") | (df['tournament'] == "UEFA Euro qualification") | (df['tournament'] == "UEFA Nations League")] # Define category 2 tournaments
    weight_category_1 = df[df['tournament'] == "Friendly"] # Define category 1 tournaments

    weight_category_3['tournament_weight'] = 3 # Assign weight 3 to category 3 tournaments
    weight_category_2['tournament_weight'] = 2 # Assign weight 2 to category 2 tournaments
    weight_category_1['tournament_weight'] = 1 # Assign weight 1 to category 1 tournaments

    weighted_df = pd.concat([weight_category_3, weight_category_2, weight_category_1]) # Combine the weighted categories back into a single DataFrame


    return weighted_df # Return the DataFrame with tournament weights assigned