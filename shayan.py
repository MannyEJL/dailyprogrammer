from math import sqrt

a = int(raw_input("a: "))
b = int(raw_input("b: "))
c = int(raw_input("c: "))

ans1 = (-b + sqrt((b**2 - 4 * a * c))) / (2 * a)
ans2 = (-b - sqrt((b**2 - 4 * a * c))) / (2 * a)

print "x1: {0} \nx2: {1}".format(ans1, ans2)
