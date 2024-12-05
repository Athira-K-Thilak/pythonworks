#  create dictionary employee with keys eid,name,salary,department,experience

employee={"id":1000,
          "name":"athira",
          "salary":35000,
          "department":"robotics",
          "experience":5}

print(employee["salary"])

employee["contact"]=234567

print(employee)

""" if experience >5 update employee salary as current_salary+10000
else current_salary+5000"""

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)

if employee['experience']>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"    

print(employee)    