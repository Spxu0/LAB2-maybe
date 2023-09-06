# Q3.	Given a list of tuples about cars and their sales, where each tuple represents a car type and number of cars sold.


#  Write a Python program to print:
# a.	the best-selling car and number of car sold
# b.	the lease selling car and number of car sold

# The best selling car:  yaris , number of car sold:  25
# The least selling car:  benz , number of car sold:  3

car_info_list =  [('benz', 3), ('camry', 10), ('yaris', 25), ('bmw', 5), ('gmc', 4)]


# a.
car=""
number=0
car ,number=max(car_info_list)
print('The best selling car:' , car , 'number of car sold:' , number)
# b.
car ,number=min(car_info_list)
print('The best selling car:' , car , 'number of car sold:' , number)
