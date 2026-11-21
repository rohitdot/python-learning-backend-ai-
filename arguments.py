def greet(name):
    print(f"hello , {name}")

def student(name , age , branch):
    print(f"my name is {name} , im {age} years old , im pursuing {branch}")

def calculate(a, b, operation="add"):
    if operation=="add":
        print(a+b)
    elif operation=="subtract":
        print(a-b)
    elif operation=="multiply":
        print(a*b)
    elif operation=="divide":
        print(a/b)
    else:
        print(a+b)

def power(base, exponent=2):
    print(base**exponent)

def  introduce(name, age, city="Bangalore"):
    print(f"my name is {name} , im {age} years old , im from {city}")

def add(*args):
    print(sum(args))

def print_student_details(**kwargs):
    if not kwargs:
        print("No student details provided.")
        return

    print("Student Details:")
    for key, value in kwargs.items():
        # Format keys like 'first_name' into 'First Name'
        formatted_key = key.replace("_", " ").title()
        print(f"- {formatted_key}: {value}")

#function calling

greet("rixi")
student("rixi",19,"cse")
calculate(1,2)
power(2,8)
introduce("rixi",19)
add(2,3,4,43,1,31)
print_student_details(
    name="Aarav Sharma", age=20, grade="A", major="Computer Science"
)


