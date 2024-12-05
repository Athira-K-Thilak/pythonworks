
number=int(input("enter a number:"))
if number%15==0:
    print("PINGPONG")
elif number%5==0:
    print("PONG")
elif number%3==0:
    print("PING")
elif number%5!=0 or number%3!=0:
    print(number)
