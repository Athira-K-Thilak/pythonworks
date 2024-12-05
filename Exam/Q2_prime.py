

#WAP to check the number is prime or not

number=int(input("enter a number:"))

is_prime=True

for i in range(2,number):

    if number%i==0:

        is_prime=False

        break

print(is_prime)
