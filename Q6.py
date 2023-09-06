# Q6.	Given the following dictionary, which maps country names to two-letter country codes (tlcc):
# tlcc = {'Saudi Arabia': 'sa', 'Kuwait': 'kw', 'Jordan': 'jo',
#         'United Kingdom': 'uk', 'Turkey':'tr', 'Australia': 'au'}

# perform the following tasks and display the results:
# 1)	Check whether the dictionary contains the key ‘Kuwait’
# 2)	Check whether the dictionary contains the key ‘Oman’
# 3)	Iterate through the key-value pairs and display them in two-column format.
# 4)	Add the key-value pair ‘Sudan’ and ‘su’. 
# 5)	Update the value for the key ‘Sudan’ to ‘sd’


tlcc = {'Saudi Arabia': 'sa', 'Kuwait': 'kw', 'Jordan': 'jo',
        'United Kingdom': 'uk', 'Turkey':'tr', 'Australia': 'au'}

# 1)
print("Kuwait"in tlcc)
# 2)
print("Oman"in tlcc)
# 3)
for x,y in tlcc.items():
    print(x,y)

# 4)    
tlcc["Sudan"]="su"
print(tlcc)
# 5)
tlcc["Sudan"]="sd"
print(tlcc)