import datetime
print(datetime.date(2018,5,22))
print("Welcome to zaidi calculator")
def add(a,b):
    sum=a+b
    print(sum)
def subtract(a,b):
    sub=a-b
    print(sub)
def multiply(a,b):
    mul=a*b
    print(mul)
def divide(a,b):
    div=a/b
    print(div)


continuation="yes"
while continuation=="yes":
    a = int(input("\nenter first number:"))
    b = int(input("enter second number:"))
    print("Choose an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter 1-4:"))
    if choice>4:
        print("enter valid input")
    elif choice<1:
        print("enter valid input")
    elif choice == 1:
        add(a,b)
    elif choice == 2:
        subtract(a,b)
    elif choice == 3:
        multiply(a,b)
    elif choice == 4:
        divide(a,b)
    continuation=input("continue?\nenter yes or no:").lower()
print("farewell my nigga")
input("Press any button to close this window.")


