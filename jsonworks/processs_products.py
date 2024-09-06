
from json import load


f=open("C:\\Users\\HP\\Desktop\\python_june_works\\jsonworks\\products.json",encoding="UTF-8")

items=load(f)

# for i in items:
    
#     print(i.get("title"))

# product_title=[i.get("title") for i in items]

# print(product_title)

# product_jwellery=[i.get("title") for i in items if i.get("category")==("jewelery")]

# print(product_jwellery)

# product_price=[i.get("title") for i in items if i.get("price")>100]

# print(product_price)

#"products range(100,150)

# product_range=[i.get("id") for i in items if i.get("price")>100 and i.get("price")<150]

# print(product_range)

#products with most number of rating

def get_rating_count(dic):
    
    return dic.get("rating").get("count")

most_rated=max(items,key=get_rating_count)

print(most_rated)

