print("Hello World")

# #DOWNLOAD multiple tile from multiple collection
# import time
# import geopandas
# import matplotlib.pyplot as plt
# import math
# from shapely.geometry import Point
# import pystac_client
# import stackstac
# import planetary_computer
# import pandas as pd

"""
An example Python file which creates random data and exports
it to a location specified in a command line argument.
"""
import argparse
import logging

import numpy as np
import pandas as pd

# set basic logging config
logging.basicConfig(level=logging.INFO)

# gather named input from argparse
parser = argparse.ArgumentParser()
parser.add_argument("--CSV_FILENAME", help="A filepath for storing a CSV data file.")
args = parser.parse_args()

# setup some rows
NROWS = 5
NCOLS = 7

logging.info("Creating the dataframe now!")

# form a dataframe using randomized data
df = pd.DataFrame(
    np.random.rand(NROWS, NCOLS), columns=[f"col_{num}" for num in range(0, NCOLS)]
)

logging.info("Exporting the dataframe to CSV at %s !", args.CSV_FILENAME)

# export the data to parquet
df.to_csv(args.CSV_FILENAME)

logging.info("Python work finished!")

print("Goodbye World")

