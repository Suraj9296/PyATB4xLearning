class Bank:
    def __init__(self,account_number,balance):
        self.balance=balance
       # self.__password ="123"
        self.__account_number = account_number

    def deposit(self,amount):
        self.balance=self.balance+amount

    def check_bal(self):
        print(self.balance)

    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed")

icici= Bank(1234,100)
icici.deposit(100)
icici.check_bal()
icici.show_me_account_number(False)

