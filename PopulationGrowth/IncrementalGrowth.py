#incremental increase method
from math import exp

init_pop = float(input('Enter the initial population: '))
avg_rate = float(input('Enter the average increase: '))
inc_rate = float(input('Enter the incremental increase: '))
y = int(input('Enter the number of years: '))

pop = init_pop

for i in range(y):
    a = i+1
    pop = init_pop + avg_rate * a + a*(a+1)/2 * inc_rate
    print(f'Population after {i+1} years is {pop}')

print(f'Total population change after {y} years is {pop}')