# Accept the number of days from the user and calculate the charge for library according to following :
#       Days                                          Price
#      Till Five days                                  2
#      Six to Ten days                                 3
#      Eleven to Fifteen days                          4
#      After Fifteen days                              5

days = int(input("Enter the number of days:"))
charge = 0
if days <= 5:
    charge = days * 2
    print("Library fees:", charge)

elif days > 6 and days <= 10:
    charge = 10 + (days - 5) * 3      # charge calculated =
    print("Library fees:", charge)

elif days > 11 and days <= 15:        # In charge calculated25 comes by:-  previous charge = 10 + (days - 5) * 3
    charge = 25 + (days - 10) * 4     #                                                      10 + (10 - 5) * 3 = 25
    print("Library fees:", charge)

else:
    charge = 45 + (days - 15) * 5
    print("Library fees:", charge)