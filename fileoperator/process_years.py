#my logic


# years=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\years.txt","r")
# centuary_years=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\centuary_years.txt","w")
# leap_years=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\leap_years.txt","w")

# for year in years:

#     year=int(year)

#     if year%4==0 and year%100!=0 or year%400==0 and year%100==0:

#         leap_years.write(str(year)+"\n")

#     if year%100==0:

#         centuary_years.write(str(year)+"\n")    

# years.close()
# centuary_years.close()
# leap_years.close()        


#2nd logic

years_path="C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\years.txt"
centuary_years_path="C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\centuary.txt"
leap_years_path="C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\leapyears.txt"

f_read=open(years_path,"r")

f_centuary=open(centuary_years_path,"w")

f_leapyear=open(leap_years_path,"w")

def is_centuray_year(year):

    return True if year%100==0 else False

def is_leap_year(year):

    return True if year%100==0 and year%400==0 or year%100!=0 and year%4==0  else False

for year in f_read:

    year=int(year)

    if is_centuray_year(year):

        f_centuary.write(str(year)+"\n")

    if is_leap_year(year):

        f_leapyear.write(str(year)+"\n")

f_read.close()

f_centuary.close()

f_leapyear.close()

