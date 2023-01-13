from fx import *

print(c.rates_)

# Developed by: Yesner...

print("=======================================")
print("||      Convert money                ||")
print("=======================================")
x = input("Enter the quantity of cordoba: ")

print("USD",c.convert(int(x), 'NIO', 'USD'))
print("NIO",c.convert(int(x), 'USD', 'NIO'))

