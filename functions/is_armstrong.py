

def is_armstrong_number(number):
        
        orginal_number=number
        
        count=len(str(number))

        total=0

        while(number>0):
                
            last_digit=number%10

            exponent=last_digit**count

            total=total+exponent

            number=number//10

        print("Armstrong number"  if total==orginal_number else "Not Armstrong")

is_armstrong_number(153)            



                


        


