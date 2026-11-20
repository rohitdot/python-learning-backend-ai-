def calculate_area(length,width):
    return length*width

def power(number,exp=2):
    return number**exp

def students(name,age,branch="cse"):
    print("NAME :",name,"branch",branch,"age",age)

def calculate_bill(p,q,d=0):
    return p+q-d


print(calculate_area(2,3))
print(power(2))
print(power(2,3))
students("rohit",12)
students("rixi",56,"ise")
students("name",any,"ise")
print(calculate_bill(2,3,4))
print(calculate_bill(2,3))