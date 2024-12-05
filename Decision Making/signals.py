
#syntax

# if condition1:
    #stmt 1

#elif condition2:
    #stmt2

#elif condition3:
    #stmt 3

#else: 
   # default stmt

signal=input("enter signal: ").lower()

if signal=="red" :
     
     print("STOP")

elif signal=="green" :

    print("GO..")

elif signal=="yellow":

         print("WAIT !") 

else:
     
     print("Invalid Signal")    