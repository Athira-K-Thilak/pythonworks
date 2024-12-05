
#dictionary methods

employee={"id":1000,"name":"ram","department":"hr","age":32,"salary":25000}

# print(employee.get("department"))
# #invalid key returns none

# pop(key)  remove
employee.pop("salary")

print(employee)

#return all keys => keys()

for k in employee.keys():

    print(k)

    # fetch all values =>values()

for v in employee.values():

    print(v) 

    # fetch key and values  => items()
for k,v in employee.items():

    print(k,v)

