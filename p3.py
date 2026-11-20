def sum(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum


def max(l):
    largest=l[0]
    for i in l:
        if i>largest:
            i=largest
    return largest

def count_v(s):
    count=0
    v="aeiouAEIOU"
    for i in s :
        if i in v:
            count+=1
    return count


def is_palindrome(s):
    return s==s[::-1]

def fac(n):
    if n<0:
        return "invalid"
    elif n==0 or n==1:
        return 1
    else :
        return n*fac(n-1)

s="hi my name is rohit"
a="riir"
print(count_v(s))
print(is_palindrome(a))
print(fac(4))