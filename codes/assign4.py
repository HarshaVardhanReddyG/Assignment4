import numpy as np
from numpy import random as RN 
#Total possible outcomes
N=6
#No. of outcomes that are prime
n_0=3
#No. of outcomes that are greater than 3
n_1=4
#No. of outcomes that are less than are equal to 1
n_2=1
#No. of outcomes that are greater than 6
n_3=0
#No. of outcomes that are less than 6
n_4=5
#respective theoritical probabilities
pr_0=n_0/N
pr_1=n_1/N
pr_2=n_2/N
pr_3=n_3/N
pr_4=n_4/N
#initialising all the frequencies to 0
x_0=0
x_1=0
x_2=0
x_3=0
x_4=0
for i in range(N):
    x = np.random.choice([i for i in range(1,7)])
    if(x == 2 or x==3 or x==5):
        x_0 += 1
    if(x>=3):
        x_1 += 1
    if(x<=1):
        x_2 += 1
    if(x>6):
        x_3 += 1
    if(x<6):
        x_4 += 1
print("Theoritical probabilities are ",pr_0,pr_1,pr_2,pr_3,pr_4)
print("Experimental probabilities are",x_0/N,x_1/N,x_2/N,x_3/N,x_4/N)
