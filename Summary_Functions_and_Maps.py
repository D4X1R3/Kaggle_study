import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("/users/arseniy/repos/datasets/winemag-data-130k-v2.csv", index_col=0)

#calculating the mean of points using the 'mean()' metod of a pandas
review_points_mean = reviews.points.mean()

#creating a function that takes a single argument row
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

newform = reviews.apply(remean_points, axis='columns')

print(newform.loc[:, ["country", 'points', 'title']])