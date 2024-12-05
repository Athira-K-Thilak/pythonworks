

"""write a dictionary comprehension to convert all the values in a dictionary 

     to their absolute value"""

#absolute value is the non negative value of a number  without regard to its sign 

#  abs() function returns  the absolute value of a specified number

dictionary={"num1":-5,"num2":3,"num3":-10,"num4":6,"num5":-2}

absolute_value_dict={k:abs(v) for k,v in dictionary.items()}

print(absolute_value_dict)