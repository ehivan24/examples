class CreditCard:

    def __init__(self, costumer, bank, account, limit, balance):
        self.costumer = costumer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = balance

    def getCostumer(self):
        return self.costumer

    def getBank(self):
        return self.bank

    def getAccount(self):
        return self.account

    def getLimit(self):
        return self.limit

    def getBalance(self):
        return self.balance

    def charge(self, price):
        if price + self.balance > self.limit:
            print("Payment Denied")
            return False
        else:
            self.balance += price
            print("Make processed")
            return True

    def makePayment(self, price):
        if self.balance < 0:
            print("You dont have to make a payment")
            return False
        else:
            self.balance -= price

if __name__ == "__main__":
    joe = CreditCard("JOE","Chase","2324234234",2500,1000)
    print (joe.getCostumer())
    joe.makePayment(300)
    print joe.getBalance()
    joe.charge(1800)
    print joe.getBalance()
