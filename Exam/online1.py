weight_in_kg=int(input("enetr your weight:"))
height_in_cm=int(input("enter your height:"))
height_in_meter=height_in_cm/100
bmi=weight_in_kg/(height_in_meter**2)
bmi=round(bmi,2)
print(bmi)
if bmi<19:
    print("Underweight")
elif bmi>=19 and bmi<25:
    print("Normal weight") 
elif bmi>=25 and bmi<=30:
    print("overweight")
elif bmi>30:
    print('obese')           