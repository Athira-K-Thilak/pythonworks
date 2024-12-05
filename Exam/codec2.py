# def next_prime(number):
#     while(number>0):
#         number+=1
#         for i in range(2,number):
#             if number%i==0:
#                 break
#             else:
#                 return number

# print(next_prime(301))                

def next_prime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
            else:
                return n

print(next_prime(301))                            