
year=int(input('Enter Year:'))



if (year%100!=0  and year%4==0) or (year%100==0 and year%400==0):

    print(f"{year} is leap year")

else:

    print(f"{year} is not a leap year")    