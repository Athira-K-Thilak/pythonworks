
products=[{"id":1,"title":"s23ultra","brand":"samsung","price":78000},
          {"id":2,"title":"a17","brand":"samsung","price":18000},
          {"id":3,"title":"m50","brand":"samsung","price":16000},
          {"id":4,"title":"pocom3","brand":"poco","price":15000},
          {"id":7,"title":"vivov50","brand":"vivo","price":25000},
          {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
          {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
          {"id":9,"title":"iphone16proplus","brand":"apple","price":150000},
          {"id":8,"title":"nokia105","brand":"nokia","price":900}]

#total number of mobiles

print(len(products))

#print mobile titles

mobile_titles=[m.get("title") for m in products ]
print(mobile_titles)

#print samsung mobiles

samsung_mobiles=[m.get("title") for m in products if m.get("brand")=="samsung"]
print(samsung_mobiles)

# highest price mobile

highest_price_mobile=max(products,key=lambda d:d.get("price"))
costly_mobile=highest_price_mobile.get("title")
print(costly_mobile)

#low  budget mobile

lowest_priced_mobile=min(products,key=lambda  d:d.get("price"))
cheap_mobile=lowest_priced_mobile.get("title")
print(cheap_mobile)

#highest price mobiles
highest_price_mobile=max(products,key=lambda d:d.get("price"))
high_price=highest_price_mobile.get("price")
costly_mobile=[p.get("title") for p in products if  p.get("price")==high_price]
print(costly_mobile)

# {nokia:1,apple:2,samsung:2}

all_brands=[p.get("brand") for p in products]
print(all_brands)
brand_count={b:all_brands.count(b) for b in all_brands}
print(brand_count)