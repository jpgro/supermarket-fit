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

plt.hist(df["Rating"])
plt.show()

#Values of the dataset are normalized to conform to normal distribution
max_sales = max(sales)
min_sales = min(sales)
sales_norm = 1/(max_sales-min_sales)* sales

#Fit data to beta distribution and save values of alpha and beta
a, b, _, _ = beta.fit(sales)
print(a, b)


#Mean, variance and standard deviation are obtained
mu_norm = a/(a+b)
var_norm = (a*b)/((a+b)**2*(a+b + 1))
desv_norm = np.sqrt(var_norm)

#Values of mu and variance of X.
mu = (max_sales - min_sales)*mu_norm+min_sales
print(mu)
var = (max_sales-min_sales)**2*var_norm
sigma = np.sqrt(var)


#Salarios
sal_cajeros = 258.25
num_cajeros = 30
dias_t = 24

sal_conserjes = 5000
num_conserjes = 20

gerente = 100000

sal_subgerente = 45000
num_subgerentes = 4

sal_almacenistas = 262.13
num_almacenistas = 40

sal_pasillo = 264.65
num_pasillos = 40

fact = 1.15

total_cajeros = sal_cajeros*num_cajeros*dias_t*fact
total_conserjes = sal_conserjes*num_conserjes*fact
total_subgerentes = sal_subgerente*num_subgerentes
total_almacenistas = sal_almacenistas*num_almacenistas*dias_t*fact
total_pasillo = sal_pasillo*num_pasillos*dias_t*fact

nomina_tot = total_cajeros + total_conserjes + total_subgerentes + total_almacenistas + total_pasillo

print(nomina_tot)

gasto_luz = 120*2000*12*2.3*30
print(gasto_luz)

ingreso = nomina_tot + gasto_luz + 1500000

omega = norm.ppf(0.01)
a_=mu**2
b_ = -2*mu*ingreso-omega**2*sigma**2
c_ = ingreso**2

N1 = (-b_ + np.sqrt(b_**2 - 4*a_*c_))/(2*a_)
N2= (-b_ - np.sqrt(b_**2 - 4*a_*c_))/(2*a_)

print(f'N1 = {N1}, N2 = {N2}.')
