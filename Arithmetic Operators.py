print('*'*10,'CHOICES','*'*10)
print('1: Addition')
print('2: Subtraction')
print('3: Multiplication')
print('4: Division') 
print('5: Exponential')
print('6: Floor')  #FLoor gives the remainder of the division without decimal points as Output
print('7: Modulus') #Modulus provides the remainder
print()

while True:
    ch=int(input(("Enter you choice: ")))
    print()

    if ch==1:
        print("You have chosen the Arithmetic Operation 'Addition'")
        print()
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        Addition= n1+n2
        print('The Sum is',Addition)
        print()

    elif ch==2:
        print("You have chosen the Arithmetic Operation 'Subtraction'")
        print()
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        Subtraction= n1-n2
        print('The Difference is',Subtraction)
        print()

    elif ch==3:
        print("You have chosen the Arithmetic Operation 'Multiplication'")
        print()
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        Multiply= n1*n2
        print(f'The Multiple of number {n1} and {n2} is',Multiply)
        print()

    elif ch==4:
        print("You have chosen the Arithmetic Operation 'Division'")
        print()
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        Division= n1/n2
        print('The Division is',Division)
        print()

    elif ch==5:
        print("You have chosen the Arithmetic Operation 'Exponetial'")
        print()
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        Exponential= n1**n2
        print('The Exponential value is',Exponential)
        print()

    elif ch==6:
        print("You have chosen the Arithmetic Operation 'Floor Division'")
        print()
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        Floor= n1//n2
        print('The Floor Division is',Floor)
        print()

    elif ch==7:
        print("You have chosen the Arithmetic Operation 'Modulus'")
        print()
        n1=int(input('Enter the first number: '))
        n2=int(input('Enter the second number: '))
        Modulus= n1%n2
        print('The Modulus is',Modulus)
        print()

    else:
        print("Sorry..., There are only '7' Arithmetic operations...")
        break
