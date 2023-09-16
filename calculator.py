First  =input("Enter the no ")
Operator =input("Enter the operator  (+,_,*,/,%) = " )
Second  =input("Enter the no ")

First =int(First )
Second =int(Second )

if Operator == "+":
    print(First  + Second )

elif Operator == "-":
    print(First  - Second)

elif Operator == "%":

    print(First  % Second )

elif Operator == "*":
    print(First  * Second )

elif Operator == "/":
    print(Frist  / Second )

else:
    print("Invalid")

