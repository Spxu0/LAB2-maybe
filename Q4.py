
# Q4.	Write a Python program to find the sum of all animals in a given dictionary.
# The total number of animals in the zoo is  13

animals_dic = {'lion': 2, 'snake': 4, 'monkey': 3, 'giraffe': 4}
print(animals_dic.items())
num=0
for c,x in animals_dic.items():
    num=num+x
print('The total number of animals in the zoo is ',sum(animals_dic.values))


