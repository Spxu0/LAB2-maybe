# Q5.	Write a Python program to print duplicate elements from a list of integers.






nums = [8, 3, 6, 6, 1, 3, 9, 8, 2, 7, 19, 21, 3]


newset=set()
for x in nums:
    if nums.count(x)>1:
        newset.add(x)
nums1=list(newset)   
print('duplicates_list = ',nums1)
