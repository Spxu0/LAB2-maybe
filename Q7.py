# Q7.	Given the following list of dictionaries representing university classes:


#  Write Python statements that perform the following tasks:
# 1)	Display the class name of the third item in classes list.
# 2)	Display the average marks for ‘OS class.
# 3)	Display the highest mark in System Analysis class.

classes = [{'name':'Computing', 'marks':[95, 46, 90]},
              {'name':'OS', 'marks':[75, 85, 81]},
              {'name':'System Analysis', 'marks':[92, 84, 95]}]
print()

# 1)
print(classes[2]["name"])
# 2)
avg=(sum(classes[1]['marks']))/len(classes[2]["marks"])
print(avg)
# 3)
highest=max(classes[2]['marks'])
print(highest)
