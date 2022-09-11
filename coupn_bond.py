class CouponBond:

    def __init__(self,principal_amount,rate,maturity,interest_rate):
        self.principal_amount = principal_amount
        self.rate = rate / 100
        self.maturity = maturity
        self.interest_rate = interest_rate / 100

    def present_value(self,x,n):
        return x / (1+self.interest_rate)**n

    def calculate_price(self):
        price = 0
        # discount the coupon payments one by one
        for i in (1,self.maturity+1):
            price = price + self.present_value(self.principal_amount * self.rate,i)

        # discount present value of principal amount
        price = price + self.present_value(self.principal_amount,self.maturity)

        return price

if __name__ == '__main__' :
    '''
       principal amount = 1000, 
        rate for return = 10%, 
        maturity = 3 years,
        market interest rate = 4%
    '''
    bond = CouponBond(1000,10,3,4)
    print(f'Price of the coupon bond is: {bond.calculate_price()}')






