class user:
    def __init__(self,Full_name,Mobile_no,Email,Address,Password):
        self.Full_name = Full_name
        self.Mobile_no = Mobile_no
        self.Email = Email
        self.Address = Address
        self.Password = Password

    def __str__(self):
        return f"Full name : {self.Full_name} \nMobile no. : {self.Mobile_no} \nEmail : {self.Email} \nAddress : {self.Address} \n Password : {self.Password}"
    
    def get_Full_name(self):
        return self.Full_name
    def set_Full_name(self,new_Full_name):
        self.Full_name = new_Full_name

    def get_Mobile_no(self):
        return self.Mobile_no
    def set_Mobile_no(self,new_Mobile_no):
        self.Mobile_no = new_Mobile_no

    def get_Email(self):
        return self.Email
    def set_Email(self,new_Email):
        self.Email = new_Email

    def get_Address(self):
        return self.Address
    def set_Address(self,new_Address):
        self.Address = new_Address

    def get_Password(self):
        return self.Password
    def set_Password(self,new_Password):
        self.Address = new_Password
