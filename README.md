# Multinational supermarket branch

## Description

A multinational supermarket chain seeks to open a new location in a place with a population of approximately 160,000 inhabitants. Therefore, it seeks to know the percentage of people it will need to convince in order to have a monthly profit of at least 1,500,000 MXN. 

## Data 

In the SuperMarketData database, data are available on earnings from transactions in another community with a similar socioeconomic level. These already include the payment of taxes, as well as the costs of purchasing the products. 

## Estimation 

Due to its great flexibility to adjust to different distributions, the beta probability density function is used to represent and model the data distribution. 

$B(\alpha, \beta) = \int_0^1 x^{\alpha - 1}{(1-x)}^{\beta - 1} dx$

The method of *maximum likelihood estimation* is used to determine the parameters of $\alpha$ and $\beta$. 

## Expenses to consider 
There is a minimum income needed of $1,500,000 + expenses needed, because having a profit of a million and a half implies that operational costs were already covered. Because product costs were already considered in the database, there only needs to be taken into account employees salaries, water and electricity bill, among other expenses. 

The total of contemplated expenses is: 

* Salaries of: (1.15 times their minimum wage respectively)
    * 40 people in warehouse 
    * 60 people which serve clients on the halls
    * 30 cashiers 
    * 20 janitors 
* A general manager with a wage of 100,000 MXN monthly
* 4 sub-managers with a salary of 45,000 MXN monthly each
* Electricity bill: It is taken into account $120 \frac{kW/h}{m^2}$ in an area of $2000 m^2$ with a cost of $ 2.3\frac{kW}{h}$
* Water: 
    * Cost per $m^3$ consumed: 169,179.28
    * Sanitation: 20,301.51
    * Sewerage: 16,197.93 
    * IVA: 33,023.79 

* Resources managing: 2,708.82 per 7 days of recolection per week

## Results 
Approximately 22.2 percent of the population would be needed to be convinced to sucesfully cover the estimated expenses and have a million and a half in profit with a propability of 0.99. 

## Ratings 
To analyze ratings in the SuperMarketData dataset, the beta distribution was used due to its flexibility. Then, the ratings column is normalized in the interval [0, 1] for parameter estimation.

Using the method of *maximum likelihood estimation*, the shape parameters $\alpha$ and $\beta$ were determined to describe the distribution of the ratings. 

The mean and variance of the beta distribution were calculated, and then sent back to the original range of ratings. This allowed for an estimation of the characteristics of the ratings. 

Finally, the probability that the mean of the ratings exceeds 8.5 was estimated using a normal approximation, with a value of 0.173. Which means that it is necessary to take measures to 
increase perception of the supermarket in the clients, and thus achieve people prefer this supermarket over others. 
