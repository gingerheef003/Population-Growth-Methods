#geometrical mean method
from math import exp

init_pop = float(input('Enter the initial population: '))
geom_mean = float(input('Enter the geometrical mean: '))
y = int(input('Enter the number of years: '))

pop = init_pop

for i in range(y):
    a = i+1
    pop = pop * (1 + geom_mean/100)
    print(f'Population after {a} years is {pop}')

print(f'Total population change after {y} years is {pop}')