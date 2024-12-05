
#BMI=weight in kg/(hight in meter)**2

weight_in_kg=int(input("enter weight in kilogram:"))

height_in_cm=int(input("enter height in cm:"))

height_in_m=height_in_cm/100

BMI=weight_in_kg/(height_in_m)**2

BMI=round(BMI)

print(BMI)

if BMI<19:
    
    print("Under Weight")

elif  BMI<25:

    print("Normal Weight")

elif BMI<30:

    print("Over Weight")

elif BMI>=30:

    print("Obese")


