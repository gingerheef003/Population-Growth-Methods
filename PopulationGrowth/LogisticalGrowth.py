#logistical curve method
from math import exp

init_pop = float(input('Enter the initial population: '))
sat_pop = float(input('Enter the saturation population: '))
rate = float(input('Enter the rate of change of population: '))
y = int(input('Enter the number of years: '))

m = (sat_pop - init_pop)/init_pop
n = -(rate * sat_pop)

for i in range(y):
    a = i+1
    pop = sat_pop / (1 + m * exp(n * a))
    print(f'Population after {a} years is {pop}')

print(f'Total population change after {y} years is {pop}')