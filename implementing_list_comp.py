'''List comprehensions
Practice
Convert each problem into a list comprehension.
1. Create a list of squares from 1 to 20.
2. Extract all even numbers from a list.
3. Extract all numbers divisible by 3.
4. Convert every string in a list to uppercase.
5. Extract words longer than 5 characters.
6. Create a list containing the lengths of all words.
7. From a list of numbers, create a list of squares only for odd numbers.
8. Flatten a nested list.'''

#1
list_of_sq=[x**2 for x in range(1,21)]
print(list_of_sq)

#2
nums=[1,2,3,4,5,6,7,8,9,10]
even_nums=[x for x in nums if x%2==0]
print(even_nums)

#3
nums_div_3=[x for x in nums if x%3==0]
print(nums_div_3)

#4
string=["hi how are you doing ","am doing fine","how about you"]
upper_string=[x.upper() for x in string ]
print(upper_string)

#5
words=["comprehension","python","shytwat","shawty","got","wat","let"]
large_words=[x for x in words if len(x)>5 ]
print(large_words)

#6
length=[len(x) for x in words]
print(length)

#7
sq_odd_nums=[x**2 for x in nums if x%2!=0]
print(sq_odd_nums)

#8
nest=[[1,2,3],[4,5,6],[7,8,9]]
flat=[x for x in nest for x in x ]
print(flat)