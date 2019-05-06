class product:
    def __init__(self,sell,buy,name,number,date):
        self.name = name
        self.buy = buy
        self.sell = sell
        self.date = date
        self.number = number

    def get_name(self):
        return self.name

    def get_sell_price(self):
        return self.sell

    def get_buy_price(self):
        return self.buy

    def get_date(self):
        return self.date

    def get_number(self):
        return self.number

    def profit(self):
        if((self.sell - self.buy) < 0):
            print("There is a loss on this trade")
            return 0
        else :
            return self.number*(self.sell - self.buy)
