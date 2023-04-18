class admin():
    def __init__(self,Food_id,Food_name,Food_quantity,Food_price,Food_discount,Food_stock):
        self.Food_id = Food_id
        self.Food_name = Food_name
        self.Food_quantity = Food_quantity
        self.Food_price = Food_price
        self.Food_discount = Food_discount
        self.Food_stock = Food_stock

    def __str__(self):
        return f"Food id : {self.Food_id} \nFood name : {self.Food_name} \nFood quandity : {self.Food_quantity} \nFood price : {self.Food_price} \nDiscount : {self.Food_discount} \nStock : {self.Food_stock}"
    

    def get_food_ID(self):
        return self.Food_id
    def set_food_ID(self,new_ID):
         self.Food_id = new_ID

    def get_food_Name(self):
        return self.Food_name
    def set_food_Name(self,new_name):
        self.Food_name = new_name

    def get_food_quandity(self):
        return self.Food_quantity
    def set_food_quandity(self,new_quandity):
        self.Food_quantity = new_quandity

    def get_food_price(self):
        return self.Food_price
    def set_food_price(self,new_price):
        self.Food_price = new_price

    def get_food_discount(self):
        return self.Food_discount
    def set_food_discount(self,new_discount):
        self.Food_discount = new_discount

    def get_food_stock(self):
        return self.Food_stock
    def set_food_stock(self,new_stock):
        self.Food_stock = new_stock





    
# obj = admin(234,"mandi","half",200,"10%",5)
# print(obj)
# obj.set_food_price(150)
# print(obj)