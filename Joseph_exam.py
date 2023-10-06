# Joseph has to attend an exam that starts in X minutes, but of course, watching shows takes priority.
# Every episode of the show that Joseph is watching is 24 minutes long.
# If he starts watching a new episode now, will he finish watching it strictly before the exam starts?
# Input:
# Take X from user
# Output:
# Print YES if joseph can give exam or print NO:-

x = int(input("Enter Exam starting minutes:"))
if x > 24:
    print("Yes, joseph can give exam")
else:
    print("No, joseph cannot give exam")
