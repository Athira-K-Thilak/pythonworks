
from json import load

f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\employee.json")

data=load(f)

for emp in data:

    print(emp)

