"""
Exercise 2: Compounded Interest
Write a program that calculates the future value of an $1,000 investment after 5 years, given
a compounded annual interest rate of 7%. Calculate how many years it take will take until
you double your initial investment given this interest rate [hint: start from the compound
interest rate formula V = D ×(1 +r)n and solve for n].
"""
def invest(present=1000,interest=7,time=5,compounds=1):
    interest/=100
    future=present*(1+(interest/compounds))**(time*compounds)
    return(future)
print(f"Future value of the intial investment: #{invest():,.2f}")
"""
Exercise 3: Net Present Value
A project requires an initial investment of $1,000 and is expected to generate cash inflows
of $400 in year 1, $300 in year 2, $500 in year 3, and $200 in year 4. The required rate of
return (discount rate) is 10% per year. Write a program that calculates the NPV. Will you
invest in this project?
"""

def NPV(discount):
    discount/=100
    net= -1000
    net += 400 / (1 + discount) ** 1
    net += 300 / (1 + discount) ** 2
    net += 500 / (1 + discount) ** 3
    net += 200 / (1 + discount) ** 4
    return(net)

x= NPV(10)
if x > 0:
    print(f"Invest. the NPV is greater than zero ({x}), and hence the investment reduces a return exceeding the required rate of return")

elif x < 0:
    print(f"Do not invest. the NPV is less than zero ({x}), and hence the investment reduces a return below the required rate of return")

