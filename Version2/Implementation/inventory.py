from functools import reduce
from product import *
class inventory:
    def __init__(self,l):
        self.inventory = l

    def add_trade(self,sell,buy,name,number,date):

        self.inventory.append(product(sell,buy,name,number,date))

    def delete_trade(self,order):

        index = 0
        count = 0
        for i in self.inventory:
            if i.get_order() == order:
                index = self.inventory.index(i)
                count += 1
        if(count != 0):
            if(count == 1):        
                self.inventory.pop(index)                
            else:
                print("There are multiple items found in inventory")

    def net_profit(self):
        profitlist = [ i.profit() for i in self.inventory]
        return reduce((lambda x, y : x+y) , profitlist)

    def toSeq(self):
        return self.inventory

    def toString(self):
        string = ""
        for i in self.inventory:
            string += i.get_name()
            string += "\nThe sell-out price:  "
            string += str(i.get_sell_price())
            string += "\nThe buy-in price:  "
            string += str(i.get_buy_price())
            string += "\nThe date:  "
            string += str(i.get_date())
            string += "\nPairs:  "
            string += str(i.get_number())
            string += "\nProfit:  "
            string += str(i.profit())
            string += "\n\n\n"
