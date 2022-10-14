import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from os import listdir
import sys

"""_summary_

    Main objective:
    extract pandas profiling from datasources csv in specific folder

Returns:
    _type_: _description_
    html pandas profiles in specific output folder
    
"""

# data folder
datafolder = "data-in/"

# html pandas profiling output folder
dataprofiles = "data-profiles/"

# file extension to filter in data folder (could be a list also ['ext1','ext2'] )
extensions = (".csv", ".xlsx")


def find_csv_filenames(path_to_dir, suffix=extensions):
    """_summary_

    Args:
        path_to_dir (_type_): path where data input exists
        suffix (_type_, optional): accepted data extensions

    Returns:
        _type_: _description_
    """
    filenames = listdir(path_to_dir)

    return [filename for filename in filenames if filename.endswith(suffix)]


datafiles = find_csv_filenames(datafolder)

for datafile in datafiles:

    dataname = datafile.split(".")[0]
    dataext = datafile.split(".")[-1]
    datafile = datafolder + datafile

    if dataext.lower() == "xlsx":
        df = pd.read_excel(datafile, index_col=False, engine="openpyxl")  # XLSX
    if dataext.lower() == "csv":
        df = pd.read_csv(datafile, low_memory=False, index_col=False)  # CSV
    print(df)

    profile = ProfileReport(df, title=f"{dataname} Profiling Report", minimal=True)
    profile.to_file(f"{dataprofiles+dataname}.html")
