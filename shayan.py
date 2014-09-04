from math import sqrt

a = int(raw_input("a: "))
b = int(raw_input("b: "))
c = int(raw_input("c: "))
ans1 = "N/A"
ans2= "N/A"

d = b**2-4*a*c
print "The discriminant is {0}".format(d)

if d<=0:
    print "No real answer"
elif d==0:
    print "One real answer"
    ans1 = (-b + sqrt(d)) / (2 * a)
    if d>=0:
        print "Two real answers"
        ans2 = (-b - sqrt(d)) / (2 * a)
        
print "x1: {0} \nx2: {1}".format(ans1, ans2)

