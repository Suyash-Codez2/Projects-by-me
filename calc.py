# Making a calculator in Python

x = float(input("Enter the number:"))
y = float(input("Enter the number:"))

print("Select Operation")
print("1. Addition\n", "2. Substraction\n", "3. Multiplication\n", "4. Division")
z = int(input("Which operation from above to choose"))

if z == 1:
    print(x+y)
elif z == 2:
    print(x-y,"\n",y-x)
elif z == 3:
    print(x*y)
else:
    print(x/y,"\n",y/x)

