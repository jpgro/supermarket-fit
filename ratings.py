import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.stats import norm 


#CSV file is read as a pandas dataframe
df = pd.read_csv("SuperMarketData.csv")

print(df.head)

#Ratings column is obtained from dataframe df
ratings = np.array(df["Rating"])

max_rating = max(ratings)
min_rating = min(ratings)
rating_normal = 1/(max_rating - min_rating) * (ratings - min_rating)

#Beta distribution
a, b, _, _ = beta.fit(ratings)
print(f'Alpha = {a}, Beta = {b}')

#Values of beta distribution are calculated
mu_normal = a/(a+b)
variance_normal = (a*b)/((a+b)**2 * (a+b+1))
desv_norm = np.sqrt(variance_normal)


mu = (max_rating - min_rating) * mu_normal + min_rating 
var = (max_rating - min_rating)**2*variance_normal
sigma = np.sqrt(var)

prob = 1 - norm.cdf(8.5, mu, sigma)
print(f'Probability that ratings mean be higher than 8.5: {prob}')