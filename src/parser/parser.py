"""
Manages parsing data into a pickle format.

Note: The CSV data is of the format:

tourney_id,tourney_name,surface,draw_size,tourney_level,tourney_date,match_num,
winner_id,winner_seed,winner_entry,winner_name,winner_hand,winner_ht,
winner_ioc,winner_age,winner_rank,winner_rank_points,loser_id,loser_seed,
loser_entry,loser_name,loser_hand,loser_ht,loser_ioc,loser_age,loser_rank,
loser_rank_points,score,best_of,round,minutes,w_ace,w_df,w_svpt,w_1stIn,
w_1stWon,w_2ndWon,w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,
l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced

** USAGE **
Since all files should be launched from the root you can use this script by:
import src.parser.parser as parser

Then
df = parser.read_year(year)

OR

all_data = parser.read_all()

NOTE: ORDER IS NOT GUARANTEED WITH READ ALL.
"""

import pandas as pd
import glob

INPUT = "data/atp_matches_{}.csv" #From root directory

def read_year(year):
    """
    Reads a specific year of data from file,
    returns a panda data frame
    """
    return _read_file(INPUT.format(year))

def _read_file(dir):
    """
    Internal method for reading a file and
    returning it as a pandas data frame
    """
    with open(dir) as f:
        return pd.read_csv(f)

def read_all():
    """
    Reads all the files inside the given directory of the correct format.
    Order is **NOT** guaranteed.
    Returns a list of pandas data frames.
    """
    return [_read_file(f) for f in glob.glob(INPUT.format('*'))]
