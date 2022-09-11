
class ZeroCouponBond:
    def __init__(self,principal_amount,maturity,interest_rate):
        # principal amount of bond
        self.principal_amount = principal_amount
        # maturity - number of years
        self.maturity = maturity
        # market interest rate
        self.interest_rate = interest_rate/100

    def present_value(self,x,n):
        return x / (1 +self.interest_rate)**n

    def calculate_price(self):
        return self.present_value(self.principal_amount,self.maturity)


if __name__ == '__main__':

    bond = ZeroCouponBond(1000,2,5)
    print("The price of the bond in dollars is: %s" %bond.calculate_price())
