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
TOURNAMENT_WEIGHTS= {
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
    df['tournament_weight'] = df['tournament'].map(TOURNAMENT_WEIGHTS).fillna(1) # Map tournament types to weights, defaulting to 1 for unknown types
    return df # Return the DataFrame with the new 'tournament_weight' column


def get_recent_form(df,team, n=5):
    """Calculates the recent form of a team based on the last n matches (5).
    
    Args:
        df (pd.DataFrame): The DataFrame containing match data.
        team (str): The name of the team to calculate form for.
        n (int): The number of recent matches to consider for form calculation.
    
    Returns:
        str: A string representing the recent form (e.g., "WWLWD").
    """
    team_matches = get_team_matches(df, team) # Get matches involving the specified team
    team_matches = team_matches.sort_values(by='date', ascending=False) # Sort matches by date in descending order
    recent_matches = team_matches.tail(n) # Get the last n matches

    form = ""
    for _, match in recent_matches.iterrows():
        if match['home_team'] == team:
            if match['home_score'] > match['away_score']:
                form += "W" # Win
            elif match['home_score'] < match['away_score']:
                form += "L" # Loss
            else:
                form += "D" # Draw
        else:
            if match['away_score'] > match['home_score']:
                form += "W" # Win
            elif match['away_score'] < match['home_score']:
                form += "L" # Loss
            else:
                form += "D" # Draw

    return form # Return the recent form string