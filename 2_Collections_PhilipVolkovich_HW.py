# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# importing required libraries
import random
import string


# creating function that will create single dictionary
def create_dict():
    # defining blank dictionary
    result = {}
    # for loop to iterate random times (random.randint will choose random number n and in range (0,n) loop will work)
    # as far as number of occurrences for the number of key:value pairs wasn't chosen I decided to set from 4 to 10
    for pair in range(random.randint(2, 26)):
        # defining key as random.choice from sequence of lowercase letter
        key = random.choice(string.ascii_lowercase)
        # defining value as random randint from 1 to 100
        value = random.randint(1, 100)
        # adding new key:value pair into result
        result[key] = value
    # function returns dictionary result
    return result


# defining function that will create list of dictionaries
def create_list_dict():
    # defining blank list
    result_list = []
    # for loop to iterate random times (random.randint will choose random number n and in range (0,n) loop will work)
    for created_dict in range(random.randint(2, 10)):
        # running create_dict() function and adding it into result_list
        result_list.append(create_dict())
    # returning result list
    return result_list


# running create_list_dict() function and assigning it to the new_list variable
new_list = create_list_dict()

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# creating blank dictionaries to store:
# intermediate key:value pair with maximum value
interm_dict = {}
# index of key:value pair
index_dict = {}
# count how many times key:value pair occurs in the list
count_dict = {}
# show resulting dictionary
result_dict = {}
# for loop to iterate through i - index and d - dict in the new_list
# enumerate function is used to get the index of the dictionary inside the new_list starting from 1'''
for i, d in enumerate(new_list, start=1):
    # for loop to iterate through key, value with the method items()
    for key, value in d.items():
        # if true that key in the interm_dict
        if key in interm_dict:
            # if true that value of this key is more than value in iterm_dict with this key
            if value > interm_dict[key]:
                # changing value of this key to the current value of the key
                interm_dict[key] = value
                # assigning index of the dict as a value to the key in index_dict
                index_dict[key] = i
                # adding 1 to value of the key in count dict
                count_dict[key] += 1
            # if values is not more than existing in interm_dict for this key just adding 1
            # to show  how many times this key occurs in the new_list
            else:
                count_dict[key] += 1
        # if key is not in the interm_dict
        else:
            # adding new key:value pair
            interm_dict[key] = value
            # adding new key:index pair
            index_dict[key] = i
            # adding new key:1 pair
            count_dict[key] = 1
# for loop to iterate through key, value with the method items() in interm_dict
for key, value in interm_dict.items():
    # if true that  value of this key in count_dict is  more than 1
    if count_dict[key] > 1:
        # than adding new key:value pair where key is created from pattern "key + _ + value of this key in the
        # index_dict and value is current value
        result_dict[f'{key}_{index_dict[key]}'] = value
    # if values is this key is not more than 1, i.e. it is 1 in our case
    else:
        # than adding new key:value pair as is
        result_dict[key] = value

# printing final result
print(result_dict)
