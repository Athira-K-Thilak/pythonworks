"""write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10

      and the values are the squares of those numbers"""



squares_of_number={num:num**2 for num in range(1,11)}

print(squares_of_number)