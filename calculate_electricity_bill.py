# 5.Write a program to calculate the electricity bill (accept number of unit from user) according to the criteria:-
#        UNIT                                                  PRICE
#    First 100 Units                                         No Charge
#    Next 100 Units                                          5 Rs Per Unit
#    After 200 Units                                         10 Rs Per Unit

Units = int(input("Enter the Units:"))
if Units <= 100:
    electricity_bill = "No charge"
    print("First 100 Units:", electricity_bill)

elif Units > 100 and Units <= 200:
    electricity_bill = (Units - 100) * 5     #[Units - 100] *5 = [200 - 100] * 5 = 500
    print("Next 100 Units:", electricity_bill)

else:
    electricity_bill = 500 + (Units - 200) * 10       # Here 500 Comes from the previous Next 100 Units electricity bill
    print("After 200 Units:", electricity_bill)

