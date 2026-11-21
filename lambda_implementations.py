'''THIS FILE IMPLEMENTS MAP FILTER AND SORTED USING LAMBDA '''

l = [1, 54, 3, 4, 42]

#MAP

cube_of_l=list(map(lambda x: x**3,l))

'''returns the cube of the given list'''

print(cube_of_l)

#FILTER

even_of_l=list(filter(lambda x:x%2==0,l))

'''returns the even numbers from the list'''

print(even_of_l)

#SORTED

sort_of_l=list(sorted(l,key=lambda x:x))

print(sort_of_l)
