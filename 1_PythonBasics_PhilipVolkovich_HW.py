# 1. create list of 100 random numbers from 0 to 1000
# importing random library
import random

# creating blank new_list
new_list = []
# with help of the for loop iterating through range (100), i.e. 100 times
for i in range(100):
    # performing append method by adding to a list random values from range 0 to 1000
    new_list.append(random.choice(range(1001)))

# 2. sort list from min to max (without using sort())
# defining first for loop for the range (from 0 to len of new_list
for i in range(len(new_list)):
    # defining by default variable swapped as False, in case inner for loop will not perform any swaps
    swapped = False
    # performing inner for loop, but for the len(new_list) - i - 1, because after each swap the biggest
    # value will appear in the end of the list
    for j in range(0, len(new_list) - i - 1):
        # if checks for every left element of the list if current value in the list is bigger then the  next one
        if new_list[j] > new_list[j + 1]:
            # if yes it performs swap and value swapped assigned to True
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
            swapped = True
    # after all the swaps were made or none of them were made we use brake to exit the loop
    if not swapped:
        break

# 3. calculate average for even and odd numbers
# assigning variables  even_sum and even_count equals to 0, the same for the odd numbers
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0
# for loop for iterating through the new_list elements
for i in new_list:
    # checking if modulus division is 0 and if True adding i element to even_sum variable and adding 1 to even_count
    if i % 2 == 0:
        even_sum += i
        even_count += 1
# if modulus division is not 0  adding i element to odd_sum variable and adding 1 to odd_count
    else:
        odd_sum += i
        odd_count += 1
# calculating  avg_even by dividing even_sum to even_count. The same for the odd
avg_even = even_sum/even_count
avg_odd = odd_sum/odd_count

# 4. print both average result in console
# using f string formatting for printing average values and the string text itself
print(f"Average even number:{avg_even}")
print(f"Average odd number:{avg_odd}")
