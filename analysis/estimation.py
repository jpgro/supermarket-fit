#October 22, 2024


#Import needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.stats import norm 


#Data is Read as a Pandas Dataframe
df = pd.read_csv("SuperMarketData.csv")

#Print data frame head
print(df.head())

#All sales converted to MXN local currency
sales = np.array(df["Sales"])*19.88

#Values of the dataset are normalized to conform to normal distribution
max_sales = max(sales)
min_sales = min(sales)
if (max_sales != min_sales): 
    sales_norm = 1/(max_sales-min_sales)* sales


#Fit data to beta distribution and save values of alpha and beta
a, b, _, _ = beta.fit(sales)
print(a, b)


#Normalized mean, variance and standard deviation are obtained
mu_norm = a/(a+b)
var_norm = (a*b)/((a+b)**2*(a+b + 1))
desv_norm = np.sqrt(var_norm)

#Not normalized mean and variance
mu = (max_sales - min_sales)*mu_norm+min_sales
var = (max_sales-min_sales)**2*var_norm
sigma = np.sqrt(var)


#Salaries
salary_cashier = 258.25
num_cashier = 30
days = 24

salary_janitor = 5000
num_janitor = 20

manager = 100000

salary_submanager = 45000
num_submanager = 4

salary_storekeeper = 262.13
num_storekeeper = 40

salary_hall = 264.65
num_hall = 40

factor = 1.15

total_cashier = salary_cashier*num_cashier* days * factor
total_janitor = salary_janitor*num_janitor*factor
total_submanager = salary_submanager*num_submanager
total_storekeeper = salary_storekeeper*num_storekeeper*days*factor
total_hall = salary_hall*num_hall*days*factor

roster = total_cashier + total_janitor + total_submanager + total_storekeeper + total_hall


#Other expenses
monthly_electricity_bill = 120*2000*12*2.3*30
monthly_water_bill = 169179.28 + 20301.51 + 16917.93 + 33023.79
monthly_residuals = 2708.82 * 4

#Minimum income required
income = roster + monthly_electricity_bill + monthly_water_bill + monthly_residuals 

#Calculation of how many people are needed to get that income level 
#with a confidence of more or equal 99%

omega = norm.ppf(0.01)
a_=mu**2
b_ = -2*mu*income - omega**2*var
c_ = income**2

N1 = (-b_ + np.sqrt(b_**2 - 4*a_*c_))/(2*a_)
N2= (-b_ - np.sqrt(b_**2 - 4*a_*c_))/(2*a_)
print(f'Results: N1 = {N1}, N2 = {N2}.')

if (income/N1 - mu > 0): 
    N = N1 
else: 
    N = N2

#Percentage of population to convince
population = 16e4
percentage_population = N / population 
print(f'Approximately {round(percentage_population, 3)}% of the population needs to be convinced. ')
