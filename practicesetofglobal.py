counter=0

def increment():
    global counter
    counter+=1
    return counter

print(increment())
print(increment())
print(increment())
print(increment())

"increments the counter by 1 everytime we call the function and returns the counter"

def counter():
    count=0

    def inc():
        nonlocal count
        count+=1
        return count
    return inc

c=counter()
print(c())
print(c())
print(c())