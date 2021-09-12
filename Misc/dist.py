'''
c = number of points on or inside a circle of centre (g,f) radius r
n = number of points given
'''
g,f,r,n = map(int, input().split())

c = 0

for i in range(n):
    x,y = map(int, input().split())
    if (x-g)**2 + (y-f)**2 <= r**2:
        c+=1

print(c)