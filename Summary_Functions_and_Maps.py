import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("/users/arseniy/repos/datasets/winemag-data-130k-v2.csv", index_col=0)


print('The average wine has', round(reviews.points.mean()), 'points.')
print('All unique tasters names are:', reviews.taster_name.unique())