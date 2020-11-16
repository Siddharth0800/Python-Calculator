print("Enter The First Number...")
a = int(input())
print("Enter The Second Number...")
b = int(input())
print("Enter The Operator...")
c = input()
if c == '+':
    print("The sum of", a, "and", b, "is", a + b)
elif c == '-':
    print("The difference of", a, "and", b, "is", a - b)
elif c == '*':
    print("The product of", a, "and", b, "is", a * b)
elif c == '/':
    print("The quotient of", a, "and", b, "is", a / b)
