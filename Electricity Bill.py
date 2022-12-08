# ELECTRICITY BILL

'''
1] If unit consumed <= 100 then cost per unit is Rs 3.50
2] If unit consumed >= 101 and <= 300 then cost per unit is Rs 7.50
3] If unit consumed >= 301 and <= 500 then cost per unit is Rs 10.00
4] If unit consumed >= 501 then the cost per unit is Rs 11.25
5] Maintenance charge is Rs 1.00 per unit.
6] Additional fixed Meter-box rent is Rs 100.
7] The tax on the bill is 20 percent which can be taken as 0.20.
'''

unit = int(input("Please enter your consumed electricity unit: "))
if unit <= 100:
    bill = unit * 3.50
elif unit >= 101 and unit <= 300:
    bill = 350 + ((unit - 100) * 7.50)
elif unit >= 301 and unit <= 500:
    bill = 350 + 1500 + ((unit - 300) * 10.00)
else:
    bill = 350 + 1500 + 2000 + ((unit - 500) * 11.25)

bill = bill + (unit*1.00)
# Bill after adding maintenance charge!

bill = bill + 100
# Bill after adding meter-box rent!

bill = bill + (bill*0.20)
# Bill after adding tax!

print("Your total bill amount is:" , bill)
print("Thank You")
