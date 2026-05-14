#Hello World
print("Hello World")

#Taking input
name = input("\033[31mEnter name:\033[0m")
#{To ANSI Escape Code used for Red text -> Begin with \033[31m and End with \033[0m}

#Formatted Strings
print(f"Hello {name}")

print(f"Hello {type(name)}")

#Conditions and nested-conditions
# if isinstance(name, str):
#     print("Name is String")
# el
if(type(name) is str):
    print("Name is String")
elif(name.isdigit()):
    print("Positive Integer entered")
else:
    try:
        if(float(name)):
            print("Decimal Value entered")
        else:
            print("Some foreign value entered")
    except ValueError:
        print("Some foreign value entered hence Value Error")


#Loops
# For in Range

for i in range(0,5):
    print(f"\x1b[32mNumber {i} being printed in for loop !!!\x1b[0m")
    #{To ANSI Escape Code used for Green text -> Begin with \x1b[32m and End with \x1b[0m}

#While
limit = 5
while(limit > 0):
    print(f"Number {5-limit} being printed in while loop !!!")
    limit -= 1

#Method in python
def print_name(name):
    print(f"Parameter {name} passed as name")

#calling a method
print_name("Alaska")


#Method with return
def print_name(name):
    return f"Parameter {name} returned as name"

#calling a method
print(print_name("Alaska"))