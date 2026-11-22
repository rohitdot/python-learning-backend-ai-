'''Topic 6: Dictionary comprehensions
Practice
1. Create a dictionary mapping numbers 1–10 to their squares.
2. Convert two lists into a dictionary.
names = ["A", "B", "C"]
marks = [80, 90, 75]

3. Create a dictionary containing only students scoring above 80.
4. Convert a list of words into a dictionary of word lengths.
5. Count character frequency using a dictionary comprehension'''

#1
nums={1:2,2:3,3:4}
dict={key:value**2 for(key,value) in nums.items() }
print(dict)

#2
names = ["A", "B", "C"]
marks = [80, 90, 75]
my_dict={name:mark for name , mark in zip(names,marks)}
print(my_dict)

