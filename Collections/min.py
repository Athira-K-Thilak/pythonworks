

expense=[12000,13000,10000,11000]

#maximum expense

# max_exp=0

# for exp in expense:

#     if exp>max_exp:

#         max_exp=exp

# print(max_exp)        

#minimum expense
# minimum=0

# min_exp=expense[0]

# for exp in range(1,4):

#     if min_exp>exp:

#         minimum=min_exp 

        
# print(minimum)        

#average

avg=0

total=0

index=len(expense)

for exp in expense:

    total+=exp

avg=total/index

print(avg)    