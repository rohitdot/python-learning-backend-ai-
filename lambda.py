square=lambda x:x**2
print(square(2))

add=lambda x,y:x+y
print(add(2,1))

if_even= lambda x : "even " if x % 2 == 0 else "odd" 
print(if_even(2))

max=lambda x,y : f"x is greater {x}" if x>y else f"y is greater {y}"
print(max(2,3))

list=[("rixi",147),("rikyu",49),("rohit",535)]
list.sort(key=lambda i: i[1])
print(list)