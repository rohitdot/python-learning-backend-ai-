'''Lambda functions
Practice
1. Create a lambda that squares a number.
2. Create a lambda that checks whether a number is even.
3. Create a lambda that returns the larger of two numbers.
4. Use lambda with map() to double every number in a list.
5. Use lambda with filter() to extract even numbers.
6. Sort a list of tuples based on the second element using lambda.'''

#1
x=(lambda x:x**2)
print(x(2))

#2
is_even=lambda x: "True" if x%2==0 else "false"
print(is_even(2))
print(is_even(3))

#3
larger=lambda x,y: f"{x}" if x>y else (f"{y}" if y>x else "equal")
print(larger(2,3))
print(larger(4,2))
print(larger(3,3))

#4
l=[1,2,3,4,5]
double=list(map(lambda x:2*x , l))
print(double)

#5
even_nums=list(filter(lambda x: x%2==0 , l))
print(even_nums)

#6
list_of_tuples=[("rohit",147,"rixi",123,"rikyu",345)]
sorted_list=sorted(list_of_tuples,key=lambda x : x[1])
print(sorted_list)