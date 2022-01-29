num1=int(input("Enter the value 1:-"))
num2=int(input("Enter the value 2:-"))
opr=input("Enter the operator value:-(only this +,_,*,/)")
'''
if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("invalid operations")
    '''
# same as elif statement
if opr == "+":
    print(num1+num2)
if opr == "-":
    print(num1-num2)
if opr == "*":
    print(num1 * num2)
if opr == "/":
    print(num1 / num2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("invalid operations")