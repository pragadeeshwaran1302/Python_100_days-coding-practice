number1=int(input("Enter the number:"))
number2=int(input("Enter the number:"))
code=int(input("Enter the code:"))
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

def main(c):
    if c==1:
        add(number1,number2)
    elif c==2:
        sub(number1,number2)
    elif c==3:
        mul(number1,number2)
    elif c==4:
        div(number1,number2)
    else:
        print("Enter the valid code between 1 to 4")

main(code)

