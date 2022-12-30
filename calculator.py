def add(num1,num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

print("Enter your choice")
print("a.Add")
print("b.Sub")
print("c.Mul")
print("d.Div")

choice = input("select your choice : ")

n1 = int(input("Enter Your First Number : "))
n2 = int(input("Enter Your Second Number : "))
def calci():
    if choice == 'a':
        print(n1, '+', n2, '=', add(n1, n2))
    elif choice == 'b':
        print(n1, '-', n2, '=', sub(n1, n2))
    elif choice == 'c':
        print(n1, '*', n2, '=', mul(n1, n2))
    elif choice == 'd':
        print(n1, '/', n2, '=', div(n1, n2))
    else:
        print("Entered Value is Invalid")






