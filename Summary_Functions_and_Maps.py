import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("/users/arseniy/repos/datasets/winemag-data-130k-v2.csv", index_col=0)

#calculating the mean of points using the 'mean()' metod of a pandas
review_points_mean = reviews.points.mean()

#faster way to see points distribution
print(reviews.points - review_points_mean)

