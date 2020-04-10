from numpy import array
from pandas import read_csv, to_numeric

def read_samples(file_name):
    return read_csv(file_name, index_col='SEQN', skip_blank_lines=True, na_values=" ").dropna().apply(to_numeric)
