#Code by Brad Menard R. Marcos - Cybersecurity Yr. 1
#Print a list - hm1
from itertools import count

fruits = ["Pineapple", "Apple", "Pear", "Grapes", "Banana"]
print(fruits)

#Access elements - hm2
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[-1])

#Modifying a list - hm3
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)

#List slicing - hm4
names = ["Alice", "Bob", "Charlie", "David", "Emma"]
subset = names[:3]
print(subset)

#Looping through a list - hm5
numbers2 = [1,2,3,4,5,6,7,8,9,10]
for x in numbers2:
    print(x**2)

#Append and extension list - hm6
shopping_cart = []
shopping_cart.append(["milk", "bread", "eggs"])
extension = ["butter", "cheese"]
shopping_cart.extend(extension)
print(shopping_cart)

#Finding max and min values - hm7
numbers = ["45", "22", "88", "56", "92", "33"]
print("Max number in list:", max(numbers))
print("Min number in list:", min(numbers))

#Counting occurences - hm8
letters = ["a", "b", "a", "c", "b", "a", "d"]
print("A spotted amount of times:", letters.count("a"))

#List comprehension - hm9
numbers2 = [1,2,3,4,5,6,7,8,9,10]
new_num2 = []
for x in numbers2:
    new_num2.append(x**2)
print(new_num2)

#List removing duplicates - hm10
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
numcheck = []
for x in nums:
    if x not in numcheck:
        numcheck.append(x)
print(numcheck)
