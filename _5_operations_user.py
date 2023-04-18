from _4_user import user
class operations_user:
    user_list = []
    def register(self):
        name = input("Enter your full name : ")
        mobile_no = input("Enter your mobile no. : ")
        email_id = input("Enter your email id : ")
        address = input("Enter your local address : ")
        password = int(input("Enter your password : "))
        user_obj = user(Full_name=name,Mobile_no=mobile_no,Email=email_id,Address=address,Password=password)
        self.user_list.append(user_obj)
        return user_obj

    order_history = []
    def login(self):
        email_id = input("Enter your registered email id : ")
        pswd = int(input("Enter your password : "))
        for i in self.user_list:
            if i.get_Email() == email_id and i.get_Password() == pswd:
                print("Sucessfully loged in")
                choice = int(input("1.Place new order  \n2.Order history  \n3.Update profile  \nChoose any option : "))
                

                if choice ==1:
                    print("Place new order")
                    menu_list = {"1":"Tandoori chicken (4 pieces) - INR 240", "2": "Vegan burger (1 piece) - INR 320", "3": "Truffle cake (500gm) - INR 900 "}
                    choice = list((input("List of foods \n1.Tandoori chicken (4 pieces) - INR 240 \n2.Vegan burger (1 piece) - INR 320 \n3.Truffle cake (500gm) - INR 900 \nselect your order")))
                    if choice!=None:
                        self.order_list=[]
                        for i in choice:
                            self.order_list.append(menu_list[i])
                             
                        print("order list")
                        
                        for i in self.order_list:
                            print("*",i)
                        confirmation = int(input("Press 1 to place the order"))
                        if confirmation==1:
                            print("Order Placed Sucessfully")
                            self.order_history.append(self.order_list)      
                        else:
                            print("items moved to wishlist")
                        return self.order_list
                    
                        
            
                      
                elif choice ==2:
                    # # self.order_history.append(self.order_list)
                    print("Order history")                   
                    for i in self.order_history:
                        print(i)
                elif choice ==3:
                    print("Update profile")
                    new_name = input("Enter updated name : ")
                    new_mobile_no = input("Enter updated mobile no. : ")
                    new_email_id = input("Enter updated email id : ")
                    new_address = input("Enter updated address : ")
                    new_pswd = int(input("Enter new password"))
                    i.set_Full_name(new_name)
                    i.set_Mobile_no(new_mobile_no)
                    i.set_Email(new_email_id)
                    i.set_Address(new_address)
                    i.set_Password(new_pswd)
                    return self.user_list
                else:
                    print("invalid input")
                


        else:
            print("invalid mail id or password")

    # def update_profile(self):
    #     new_name = input("Enter updated name : ")
    #     new_mobile_no = input("Enter updated mobile no. : ")
    #     new_email_id = input("Enter updated email id : ")
    #     new_address = input("Enter updated address : ")
    #     new_pswd = int(input("Enter new password"))
    #     i.set_Full_name(new_name)
    #     i.set_Mobile_no(new_mobile_no)
    #     i.set_Email(new_email_id)
    #     i.set_Address(new_address)
    #     i.set_Password(new_pswd)