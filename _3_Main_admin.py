from _2_operations_admin import Operaions

class Admin:
    def admin_in(self,Choice):
        if Choice == 1:
            print("Add new food ")
            operations_obj.add_new_food()
        elif Choice == 2:
            print("Edit food item using id ")
            operations_obj.editfoodBy_ID()
        elif Choice ==3:
            print(" food menu")
            operations_obj.viewmenu()
        elif Choice ==4:
            print("Remove food item using id")
            operations_obj.removeBy_ID()


if __name__ == "__main__":
    operations_obj = Operaions()
    admin_obj = Admin()
    while(True):
        admin_obj.admin_in(int(input("1.ADD NEW FOOD \n2.EDIT FOOD ITEM \n3.VIEW FOOD MENU \n4.REMOVE FOOD \nSelect an option : ")))