"""
Python Exercises
========================================================
Exercise 1: Bond Price and If Statements
Consider a bond with a par value of $1,000, 3 year maturity, 4% market interest rate and a
coupon rate of 5% (for simplicity assume that the coupon is paid annually). Calculate the
price of this bond and write a conditional if statement which 1) prints ”The bond trades
above par” if the price is above par, 2) ”The bond trades at par” if it trades at par, and
3) ”The bond trades below par” if the price is below par. Run this code a few times for
different values of the market interest rate.
========================================================"""
def bondpricer(par,TTM,YTM,CR):
    YTM/=100
    CR/=100
    coupon=par*CR
    pBond= (coupon/YTM)*(1-(1/(1+YTM)**TTM)) + par*(1/(1+YTM)**TTM)
	return(pBond)

def bondchecker(realprice,par=1000):
    if realprice > par:
        return(1)
    elif abs (realprice-par) <1e-6: #this is purely due to mechanical technicalities. £5.000000000001 tehcnically isnt equal to £5
        return(2)
    elif realprice < par:
        return(3)
price = bondpricer(1000,3,4,5)    
pricevalue = bondchecker(price)
if pricevalue == 1:
    print(f"The bond price is {price:,.2f} and hence trades above par.")
if pricevalue == 2:
    print("The bond trades at par and hence it's price is {price:,.2f}.")
if pricevalue == 3:
    print("The bond price is {price:,.2f} and hence trades below par")
"""
========================================================
Exercise 2: Lists- basic operations
1. Create a list bond prices with the following bond prices: $950, $980, $1000, and $1020.
2. Use the ’append’ function to add a bond priced at $1075 to the list.
3. Print the prices of the second and third bond to the console.
4. Add a new bond, priced at $990 in between bonds priced at $980 and $1000.
========================================================
"""
bondPrices = [950, 980, 1000, 1020]
bondPrices.append(1075)
print(bondPrices[1:3])
bondPrices.insert(2, 990)

"""
========================================================
Exercise 3: Bond Pricing with Spot Curve
Consider a fixed-coupon bond with the following characteristics:
• Face value: $1000
• Coupon rate: 6% (annual payments)
• Maturity: 6 years
The benchmark spot rate curve is given as:
spotrates = [0.030, 0.032, 0.035, 0.040, 0.042, 0.045]
Assume a constant credit spread of 1 percentage point. Use this to compute risky discount
rates for pricing the bond.
1. Compute the price of the bond using the risky spot rate curve.
2. Suppose the 1-year spot rate falls by 1 percentage point (all other rates remain un
changed). How did the price change?
3. Now suppose instead that the 6-year spot rate falls by 1 percentage point (with all
other rates unchanged). How did the price change? Why is the change different than
in the previous point?
========================================================
"""
spotrates = [0.030, 0.032, 0.035, 0.040, 0.042, 0.045]
creditspread = 0.01
def bondcalc(face,CR,TTM):
	CR/=10
	coupon=CR*face
	bPrice=0
	for i in range(TTM):
		r=spotrates[i]+creditspread
		bPrice+=(coupon/((1+r)*(i+1)))
	bPrice+=(face/((1+r)*TTM))
	return(bPrice)
print(f"The bond price is ${bondcalc(1000,6,6):,.2f}.")
