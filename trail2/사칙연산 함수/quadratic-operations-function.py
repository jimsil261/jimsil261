a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def addition(a,c):
    return a+c
def subtraction(a,c):
    return a-c
def multiplication(a,c):
    return a*c
def division(a,c):
    return a/c
if o in ["+","-","*","/"]:
    if o=="+":
        print("%d + %d = %d" %( a,c,addition(a,c)))
    elif o=="-":
        print("%d - %d = %d" % (a,c,subtraction(a,c)))
    elif o=="*":
        print("%d * %d = %d" % (a,c,multiplication(a,c)))
    else:
        print("%d / %d = %d" % (a,c,division(a,c)))
else:
    print("False")