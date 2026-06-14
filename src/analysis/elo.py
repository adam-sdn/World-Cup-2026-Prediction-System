"""


elo.py

Gives an updated ELO Rating for each team based on the match results. This is used as a feature in the predictor model.
Gets data from the results_clean.csv file from data\processed created by export.py


ELO Rating Formula : 
New Rating = Old Rating + K x (Actual Result - Expected Result)

Output: the following is generated :
    
    elo_ratings.csv - A CSV file containing the ELO ratings for each team, saved in data/processed/elo_ratings.csv 
    (used for Poisson Model predictions and as a feature in the predictor model)

    elo_history.csv - Used for the graph visualisation and chartings of ELO ratings over time saved in data/processed/elo_history.csv

"""

import pandas as pd
import os
from src.data.export import load_processed_match_results


ELO_RATINGS_PATH = "data/processed/elo_rating.csv"
ELO_HISTORY_PATH = "data/processed/elo_history.csv"

#Initilaising the base value for ELO Ratings
ELO_BASE_RATING = 1000


#K-Factors for different match types based on their value and global importance. Higher K-Factor means more impact on ELO ratings.
K_FACTORS = {
    "FIFA World Cup": 60,
    "UEFA Euro": 60,
    "Copa América": 60,
    "Africa Cup of Nations": 60,
    "FIFA World Cup qualification": 40,
    "UEFA Euro qualification": 40,
    "UEFA Nations League": 40,
    "Friendly": 20
}