def add(a,b):
    return a+b

def sq(a):
    return a**2

def is_even(a):
    if (a%2==0):
        print("EVEN")
    else:
        return 

def max(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return

def far(a):
    return (a*1.8)+32

print(add(1,2))
print(sq(2))
is_even(2)
is_even(3)
a=int(input("ENTER A:"))
b=int(input("ENTER b:"))
print(max(a,b))