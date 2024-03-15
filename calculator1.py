def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x*y

def div(x,y):
    if y != 0 :
        return x/y
    else :
        print("Enter valid value")    
        return None
choice = '''1 for sum
2 for subtraction
3 for multiplication
4 for division
5 for exit'''

while True :
    print(choice)
    c = int(input("enter your choice : "))
    if c >= 5:
        print("*****************")
        break
    x = float(input("enter the first number: "))
    print("*************")
    y = float(input("enter the second number: "))

    if c == 1 :
        print("The sum of Num {x,y} is: ", x+y )
        add()
    elif c == 2 :
        print("The subtraction of Num {x,y} is: ",x-y )
        sub()
    elif c == 3 :
        print("The Multiplication of Num {x,y} is: ",x*y )
        mul()
    elif c == 4 :
        print("The Division of numbers is: ", x/y)
        div()
    else:
        print("enter valid option")
    