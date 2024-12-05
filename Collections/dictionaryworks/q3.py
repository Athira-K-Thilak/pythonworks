
"""given a dictionary where the keys are student names and the values are their scores,
    wap to calculate the average score"""

dictionary={"Ann":35,"Ram":45,"Manu":38,"Neeraja":49,"Meenu":39}

sum=0
count=0

for v in dictionary.values():

    count+=1 #5

    sum+=v  # 35+45+38+49+39=206

average=sum/count  # 206/5=41.2

print(average)



