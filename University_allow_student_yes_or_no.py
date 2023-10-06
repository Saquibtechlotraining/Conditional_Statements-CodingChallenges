# A University allows students to sit in the exam despite of insufficient attendance if the student's attendance
# is short due to some medical cause. Take Input from User whether he had medical cause (Y/N)
# and print the message you are allowed if medical cause == Y otherwise print you are not allowed.

medical_cause = input("Enter whether the medical cause(Y/N)")
if medical_cause == "Y":
    print("You are allowed")
else:
    print("Not allowed")