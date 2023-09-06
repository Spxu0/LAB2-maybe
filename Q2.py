# Q2.	Write a Python program to 1) print the first and last fruits and 2) print any fruit that contains letters p and e in its name from the following fruit list.



# output:
# fruit list =  ['orange', 'banana', 'kiwi', 'peach', 'watermelon', 'apple']
# first fruit is  orange
# last fruit =  apple
# fruits contains p and e:  ['peach', 'apple']
    
fruit_list = ["orange", "banana", "kiwi", "peach", "watermelon", "apple"] 

print("fruit_list = ",fruit_list)
print("First fruit is ",fruit_list[0])
print("Last fruit =",fruit_list[-1])
fruit_list.count

list2=[]

for x in fruit_list:
    if x.count("p") and x.count("e"):
        list2.append(x)
print("fruits contains p and e:",list2)
        