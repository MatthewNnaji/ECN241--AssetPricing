time=int(input("Enter maturity length："))
par=int(input("Enter face value："))
IR=float(input("Enter current IR："))
IR=IR/100
coupon=IR*par

pay= [coupon]*(time-1) + [par+(coupon)]
def delibird(durate=0,year=time,YTM=IR):
    SV = 0
    Per = []
    discount = 1/(1+YTM)
    for i in range(year-durate):
        SV=coupon * discount**(i+1)
        Per.append(SV)
	
    SV = par/((1+YTM)**(year-durate))
    m = Per[-1] + SV
    Per[-1] = m
    return(Per)


y=delibird()
z=y.copy()
index=0
statement= f"Present value of all annualised fixed payments are as follows, from Y1 to Y{time}: ["
for i in range(len(z)-2):
    z[i]= round(z[i],1)
    index=i+1
    statement+= "£"+str(z[i])+"("+str(index)+"), "
z[-2]= round(z[-2],1)
z[-1]= round(z[-1],1)
statement+=  "£"+str(z[-2])+"("+str(len(z)-1)+") and £"+str(z[-1])+"("+str(len(z))+")]"
print(statement)

nominalstatement= f"Nominal value of all annualised fixed payments are as follows, from Y1 to Y{time}: ["
for i in range(len(z)-2):
    nominalstatement+= "£"+str(coupon)+"("+str(index)+"), "
nominalstatement+=  "£"+str(coupon)+"("+str(len(z)-1)+") and £"+str(par+coupon)+"("+str(len(z))+")]"
print(nominalstatement)
sellyear=int(input("Enter remaining time to maturity"))
while sellyear < 0 or sellyear > time:
    sellyear=int(input("Incorrect. enter valid number"))
verify=int(input("Has the interest rate changed? Enter 1 for 'True' or 0 for 'False': "))
while verify != 0 and verify != 1:
    verify=int(input("Incorrect. Enter 1 for 'True' or 0 for 'False': "))
if verify == 1:    
    newIR=float(input("enter the new interest rate"))
    while newIR <= 0:
        sellyear=int(input("Incorrect. enter valid number"))
    newIR= newIR/100



    
if sellyear == 0:
    print(f"present value is £{par}, And by holding to maturity your return rate is {IR}%.")
else:
    x= delibird(time-sellyear,time,newIR)
    profit = coupon * (time-sellyear)
    profit += sum(x)-par
    profit /= par
    profit = (1+profit)**(1/(time-sellyear))
    profit -= 1
    roundPV=str(round(sum(x),2))
    roundProfit=str(round(profit*100,2))
    print(f"present value is £{roundPV}. If you sold now, your return rate would be {roundProfit}%.")




"""
time=int(input("Enter maturity length："))
par=int(input("Enter face value："))
IR=float(input("Enter current IR："))
IR=IR/100
coupon=IR*par

pay= [coupon]*(time-1) + [par+(coupon)]
def delibird(durate=0,year=time,YTM=IR):
    SV = 0
    Per = []
    for i in range(year-durate):
        print(i+1)
        SV=coupon/((1+YTM)**(i+1))
        print(SV)
        Per += [SV]
        print(Per)
        print("---")
	
    SV = par/((1+YTM)**(year-durate))
    m = Per[-1] + SV
    Per[-1] = m
    print("====")
    print(Per)
    print(pay)
    print("fin looopppppppppppp")
    print(sum(Per))
    return(Per)

delibird()
sellyear=int(input("Enter remaining time to maturity"))
while sellyear < 0 or sellyear > time:
    sellyear=int(input("Incorrect. enter valid number"))
verify=int(input("Has the interest rate changed? Enter 1 for 'True' or 0 for 'False': "))
while verify != 0 and verify != 1:
    verify=int(input("Incorrect. Enter 1 for 'True' or 0 for 'False': "))
if verify == 1:    
    newIR=float(input("enter the new interest rate"))
    while newIR <= 0:
        sellyear=int(input("Incorrect. enter valid number"))
    newIR= newIR/100



    
if sellyear == 0:
    print("present value is",par,"And by holding to maturity your return rate is",IR)
else:
    x= delibird(time-sellyear,time,newIR)
    y=0
    print(x)
    print("AAAA")
    profit = coupon * (time-sellyear)
    print(profit)
    profit += sum(x)-par
    print(profit)
    profit /= par
    print(profit)
    profit = (1+profit)**(1/(time-sellyear))
    print(profit)
    profit -= 1
    print("present value is",sum(x),"If you sold now your return rate would be",profit*100)
"""
