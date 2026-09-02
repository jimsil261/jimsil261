product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code
class Product:
    def __init__(self,product_name,product_code):
        self.product_name=product_name
        self.product_code=product_code

p1=Product("codetree",50)
p2=Product(product_name,product_code)

print("product %d is %s" %(p1.product_code,p1.product_name))
print("product %d is %s" %(p2.product_code,p2.product_name))