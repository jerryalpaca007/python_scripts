def bubblesort(products):
    p_list=list(products)
    n=len(p_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if p_list[j][1]>p_list[j+1][1]:
                p_list[j],p_list[j+1]=p_list[j+1],p_list[j]
    return tuple(p_list)
np=int(input(""))
products=()
for i in range(np):
    name=input("product name:")
    price=float(input("price:"))
    expiry=input("expiry DD/MM/YYYY:")
    prod=(name,price,expiry)
    products=products+(prod,)
s_products=bubblesort(products)
for prod in s_products:
    print(prod)