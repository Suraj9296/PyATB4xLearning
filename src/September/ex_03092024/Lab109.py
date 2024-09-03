class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_confirm(self):
        if self.email == "suraj@gmail.com" and self.password =="Pass123":
            print("Allowed to login")
        else:
            print("not allowed")

email = input("enter the email\n")
password = input("enter the password\n")

vm_obj=VWOLoginPage(email,password)
vm_obj.login_confirm()

