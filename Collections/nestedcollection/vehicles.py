  

cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

#print count of vehicles

print(f"total vehicles=>{len(cars)}")

#print  available colors of baleno

baleno_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]
print(baleno_colors[0])

#print all brands
brand_name={c.get("brand") for c in cars }
print(brand_name)

#or 

all_brands=[c.get("brand") for c in cars]
print(set(all_brands))

#print car names available in amt transmission

amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_cars)

#cars available in blue colors

blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]
print(blue_cars)

#print all transmissions
all_transmissions={t for c in cars for t in c.get("transmissions")}
print(all_transmissions)

#print all colors
all_colors={colors for c in cars for colors in c.get("colors")}
print(all_colors)

#print most popular colors

# popular_color={p:p for c in cars for p  in  c.get("colors")}
# print(popular_color)

#costly car
highest_price_car=max(cars,key=lambda c:c.get("price"))
costly_car=highest_price_car.get("name")
print(costly_car)

#car with minimum cost
minimum_cost_car=min(cars,key=lambda m:m.get("price"))
cheapest_car=minimum_cost_car.get("name")
print(cheapest_car)

#sort cars wrt price
sorted_cars=sorted(cars,key=lambda d:d.get("price"))# ascending order
sorted_car_name=[c.get("name") for c in sorted_cars]
print(sorted_car_name)

sorted_cars=sorted(cars,key=lambda d:d.get("price"),reverse=True)# descending order
sorted_car_name=[c.get("name") for c in sorted_cars]
print(sorted_car_name)

sorted_cars=sorted(cars,key=lambda d:d.get("price"),reverse=True)# dictionary key value pairs
sorted_car_name={c.get("name"):c.get("price") for c in sorted_cars}
print(sorted_car_name)

sorted_cars=sorted(cars,key=lambda d:d.get("price"),reverse=True)# dictionary key value pairs more than values using list
sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_cars}
print(sorted_car_name)


