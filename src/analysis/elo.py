"""


elo.py

Gives an updated ELO Rating for each team based on the match results. This is used as a feature in the predictor model.
Gets data from the results_clean.csv file from data\processed created by export.py


ELO Rating Formula : 
New Rating = Old Rating + K × (Actual Result - Expected Result)

Output: the following is generated :
    
    elo_ratings.csv - A CSV file containing the ELO ratings for each team, saved in data/processed/elo_ratings.csv 
    (used for Poisson Model predictions and as a feature in the predictor model)

    elo_history.csv - Used for the graph visualisation and chartings of ELO ratings over time saved in data/processed/elo_history.csv

"""

import pandas as pd
import os
from src.data.export import load_processed_match_results


ELO_BASE_RATING = 1000