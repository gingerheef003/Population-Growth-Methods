#exponentail growth method
from math import exp

init_pop = float(input('Enter the initial population: '))
rate = float(input('Enter the rate of change of population: '))
y = int(input('Enter the number of years: '))

pop = init_pop

for i in range(y):
    a = i+1
    pop = init_pop * exp(rate * a)
    print(f'Population after {a} years is {pop}')

print(f'Total population change after {y} years is {pop}')