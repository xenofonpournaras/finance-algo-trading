from math import exp


def future_discrete_value(x,r,n):
    return x*(1+r)**n

def present_discrete_value(x,r,n):
    return x//(1+r)**n

def future_continuous_value(x,r,n):
    return x*exp(r*n)

def present_continuous_value(x,r,n):
    return x//exp(r*n)

if __name__ == '__main__':

    x = float(input("Enter initial amount of money: "))
    r = float(input("Enter interest rate: "))
    n = float(input("Enter number period of time (in years): "))

    future_discrete_value = future_discrete_value(x,r,n)
    present_discrete_value = present_discrete_value(x,r,n)
    future_continuous_value = future_continuous_value(x,r,n)
    present_continuous_value = present_continuous_value(x,r,n)
    
    print("Future value for discrete model of x: %s" % future_discrete_value)
    print("Present value for discrete model of x: %s" % present_discrete_value )
    print("Future value for discrete model of x: %s" % future_continuous_value)
    print("Present value for discrete model of x: %s" % present_continuous_value)

