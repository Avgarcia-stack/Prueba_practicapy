print("Welcome to my calculator program!")
print("this program can perform basic arithmetic operations.")
print("Please enter the first number:")
x = float(input())
print("Please enter the second number:")
z = float(input())
N = (x + z)
X = (x - z)
Y = (x * z)
Z = (x / z)
F = (x ** z)
P = (x % z) 

selection = input("Please Select ur operation: +, -, *, /, **, % : ")
valid_options = ["+", "-", "*", "/", "**", "%"]
if selection == "+":
    print("The Sum is : ", N)

elif selection == "-":
    print("The Subtract is : ", X)
elif selection == "*":
    print("The multiply is: ",Y)
elif selection == "/":
     print("The Divide is : ", Z)
elif selection == "**":
     print("The elevate is : ", F)
elif selection == "%":
     print("The Porcentage is : ", P)
if selection in valid_options:
    pass
else:
    while selection not in valid_options:
        print("Opción incorrecta. Intenta de nuevo.")
        selection = input("Elige una operación: +, -, *, /, **, %: ")

# Aquí selection ya es válida
if selection == "+":
    print("La suma es:", N)
elif selection == "-":
    print("La resta es:", X)
elif selection == "*":
    print("La multiplicación es:", Y)
elif selection == "/":
    print("La división es:", Z)
elif selection == "**":
    print("La potencia es:", F)
elif selection == "%":
    print("El residuo es:", P)