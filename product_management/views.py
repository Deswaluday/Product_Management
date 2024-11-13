from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Product:
    def __init__(self):
        pass
   
    def getprice_seasonal(self,price):
        Seasonal_value = price
        return Seasonal_value
        
    def getprice_bulk(self,price):
       
        Bulk_value = price
        return Bulk_value

    def get_percentage_dis(self,dis_value,price):
        dis_p = price * dis_value/100
        return dis_p


class Seasonal_price(Product):

     def __init__(self):
        pass
    
     def fixed_discount(self,dis_amount,dis_type,price):
        s_price = Product.getprice_seasonal(self,price)
        if dis_type == "fixed":
            final_price = s_price-dis_amount
        else:
            p_price = Product.get_percentage_dis(self,dis_amount,s_price)
            final_price = s_price-p_price
        return final_price


class bulk_price(Product):
    def __init__(self):
        pass

    def per_discount(self,dis_amount,dis_type,price):
        print(dis_amount,dis_type,price )
        
        s_price = Product.getprice_bulk(self,price)
        if dis_type == "fixed":
            final_price = s_price-dis_amount
        else:
            p_price = Product.get_percentage_dis(self,dis_amount,s_price)
            final_price = s_price-p_price
        return final_price



class discount(Seasonal_price,bulk_price):
    def __init__(self):
        pass

    def discount_manage(self,pro_type,dis_typ,price,dis_amount):
        
        if pro_type == "bulk":
         
            final_out= discount.per_discount(self,dis_amount,dis_typ,price)
            
        else:
            final_out= discount.fixed_discount(self,dis_amount,dis_typ,price)
        return final_out


class order(discount,Product):
    def __init__(self):
        pass

    def order_manage(self):
        stock_type = (input("Enter the stock type whether it is a Seasonal or it is a Bulk : ",)).lower()
        price = int(input("Enter the price to which you want to sold the seasonal items : ",))
        discount = (input("Enter the type of discount you want to apply Percentage or Fixed : ",)).lower()
        discount_amount = int(input("Enter the discount amount : ",))

        output = order.discount_manage(self,stock_type,discount,price,discount_amount)
        return output

class MyView(View):
    def get(self, request):
        abc = order()
        print(abc.order_manage())
        return HttpResponse("result")


