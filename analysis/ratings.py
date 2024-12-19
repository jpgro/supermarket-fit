#Import needed libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.stats import norm 


#CSV file is read as a pandas dataframe
df = pd.read_csv("SuperMarketData.csv")


#Ratings column is obtained from dataframe df
ratings = np.array(df["Rating"])

#Maximum and minimum are obtained
max_rating = max(ratings)
min_rating = min(ratings)

#Ratings vector is normalized
rating_normal = 1/(max_rating - min_rating) * (ratings - min_rating)

#Beta distribution
a, b, _, _ = beta.fit(ratings)
print(f'Alpha = {a}, Beta = {b}')

#mean, variance and standard deviation of beta distribution are calculated
mu_normal = a/(a+b)
variance_normal = (a*b)/((a+b)**2 * (a+b+1))
desv_norm = np.sqrt(variance_normal)

#Converting Beta distribution parameters back to the original
#rating scale  
mu = (max_rating - min_rating) * mu_normal + min_rating 
var = (max_rating - min_rating)**2*variance_normal
sigma = np.sqrt(var)

#Probability that the mean of the ratings is greater than 8.5
prob = 1 - norm.cdf(8.5, mu, sigma)
print(f'Probability that ratings mean be higher than 8.5: {round(prob, 3)}')