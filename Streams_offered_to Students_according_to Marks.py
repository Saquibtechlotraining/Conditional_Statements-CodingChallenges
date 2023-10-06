# An institution has decided to admit new candidates in different streams on the following criteria:
# Total Marks Obtained                               Streams Offered
# 300 and above                                          Science
# 200 and above but less than 300            Commerce
# Below 200 but not below 75                    Arts
# Otherwise                                                  Admission is not granted,
#                                                        You have to appear in qualifying examination
# Write a program to input total marks obtained in an examination and print the stream allotted on the basis of above
# criteria.

marks = int(input("Enter the students marks:"))
if marks >= 300:
    stream_offered = "Science"
    print("Stream Alloted:", stream_offered)

elif marks >= 200 and marks < 300:
    stream_offered = "Commerce"
    print("Stream Alloted:",stream_offered)

elif marks >= 75 and marks < 200:
    stream_offered = "Arts"
    print("Stream Alloted:",stream_offered)

else:
    print("Admission is not granted, You have to appear in qualifying examination")