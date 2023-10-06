# You need to set a pin for your computer but there are certain rules that your pin should have to be a valid pin for your machine.
# 1.It should have only numbers
# 2.It should have any of these three symbols [&@#]
# 3.It should have more than 10 characters.

pin = input("Enter the pin:")
if pin.isnumeric:
    pin.replace(" ", "").replace("-", "")
    if len(pin) > 10:
        if ("&" in pin or "@" in pin or "#" in pin):
            print("Valid Pin")
        else:
            print("symbol character missing")

    else:
        print("Invalid length")

else:
    print("Invalid pin")