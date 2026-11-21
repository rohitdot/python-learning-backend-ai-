def is_even(num):
    '''check and return true if a number is even'''
    if num%2==0:
        return True
    return

def find_max(a,b,c):
    '''returns the largest number '''

    if a>b and a>c:
        return a 
    
    elif b>a and b>c:
        return b

    elif c>a and c>b:
        return c
    
    else:
        return "equal"

def factorial(n):
    '''return the factorial of the given number '''
    if n<0:
        return "invalid"
    
    elif n==0 or n==1:
        return 1
    
    else:
        return n*factorial(n-1)

def count_vowels(string):
    vowels="AEIOUaeiou"
    count=0
    for i in string:
        if i in vowels:
            count+=1
    return count

def reverse_string(string):
    return string[::-1]

def is_palindrome(string):
    return string == reverse_string(string)

string="HI HOW ARE YOU DOING?"

print(is_even(2))
print(find_max(21,4355,31))
print(factorial(67))
print(count_vowels(string))
print(reverse_string(string))
print(is_palindrome(string))
