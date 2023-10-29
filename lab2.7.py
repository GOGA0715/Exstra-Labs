a = int(input())
b = int(input())
c = int(input())

d = (b**2) - (4*a*c)
l = 2 * a

if d == 0:
    print(-b/(2*a))
elif d > 0:
    print((-b + (d**(1/2))) / l, (-b - (d**(1/2))) / l)
