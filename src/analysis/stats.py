"""

stats.py

Handles saving and loading processed match data.
Loads the cleaned DataFrame from export.py and provides functions to compute statistics like win/loss ratios, average goals, and performance trends.
Defines constants for statistical analysis, such as tournament weightings.


"""


import pandas as pd
from data.export import load_processed_match_results


# Constants for stats.py
STATS_FROM_2018 = 2018


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

