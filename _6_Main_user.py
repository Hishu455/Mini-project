from _5_operations_user import operations_user

class main:
    def execute(self,choice):
        if choice ==1:
            print("register")
            oper_obj.register()
        elif choice ==2:
            print("log in")
            oper_obj.login()

main_obj = main()
oper_obj = operations_user()
while True:
    choice = int(input("1.Register \n2.Login \nEnter : "))
    main_obj.execute(choice=choice)