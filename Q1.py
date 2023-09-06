# Q1.	Given the numbers: 4, 8, 34, 12, 95, 1, 14, write a proper Python statement for each of the following tasks:
# a.	Create a list from the numbers
# b.	Remove the item with the value 8
# c.	Sort the list in descending order
# d.	Remove the item in index 2
# e.	Insert 3 at the beginning of the list 

# a.
numbers=[4, 8, 34, 12, 95, 1, 14]
# b.
numbers.remove(8)
# c.
numbers.sort()
numbers.reverse()
# d.
numbers.pop(2)
# e.
numbers.insert(0,3)
print(numbers)