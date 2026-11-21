#LIST COMPREHENSION

'''--->list comprehension is a block or code snippet which is used to create a new list with shorter syntaxes using a given list'''

nums=[1,2,3,4,5,6,7,8,9,10]
even_nums=[x for x in nums if x%2==0]
print(even_nums)
'''inserts all the even number from the given list to a new list'''

# syntax ---> newlist = [expression for item in iterable if condition == True]

newlist=[x for x in range (3) ] 
'''creates a list of elements 0,1,2'''
print(newlist)

num1=[int(input(f"enter your number "))for i in range(5)]
'''creates a user input list in one line'''
print(num1)

#DICTIONARY COMPREHENSION
'''SYNTAX---> dictionary = {key:expression for (key,value) in iterable}'''

cities_in_f={'new york':71, 'chicage':32 , 'new jersey' : 34}

cities_in_c={key:((value-32)*(5/9)) for (key,value) in cities_in_f.items()}
print(cities_in_c)
'''it is used to create a new dictionary with the help of an existing dictionary of new items'''

weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather={key : value for (key,value) in weather.items() if value=="sunny" }
print(sunny_weather)
'''used to create a filtered dictionary from an existing dictionary'''

'''IMPORTANT TYPES
Basic transformation:
{key: expression for (key, value) in iterable} 

With filtering:
{key: expression for (key, value) in iterable if conditional} 

With conditional logic (if/else):
{key: (if_expression if condition else else_expression) for (key, value) in iterable} 

Using functions:
{key: function(value) for (key, value) in iterable} 
'''
