# Find GCD and LCM of two numbers

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function to find GCD (HCF)
a = num1
b = num2

while b != 0:
    a, b = b, a % b

gcd = a

# Find LCM
lcm = (num1 * num2) // gcd

# Output
print("GCD is:", gcd)
print("LCM is:", lcm)
