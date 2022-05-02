import pandas as pd
import numpy as np


def get_lower_and_upper_bounds(, multiplier):
    '''
    Takes in a dataframe column (pd.Series) and a scalar multiplier,
    returns lower and upper bounds for outlier detection'''
    q1 = df.col.quantile(.25)
