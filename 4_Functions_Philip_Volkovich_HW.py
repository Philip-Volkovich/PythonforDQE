# HW 2
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# importing required libraries
import random
import string
from typing import List


# creating function that will create single dictionary
def create_dict(min_key_num=2, max_key_num=26, min_value=0, max_value=100) -> dict:
    """This function creates random dictionary and accepts the following parameters:\n
    min_key_num - for the minimum number of key elements, by default 2.\n
    max_key_num - for the maximum number of key elements, by default 26.\n
    min_value - for the minimum value for created key:value element, by default 0.\n
    max-value - for the maximum value for created key:value element, by default 100."""
    # defining blank dictionary
    result = {}
    # for loop to iterate random times (random.randint will choose random number n and in range (0,n) loop will work)
    for pair in range(random.randint(min_key_num, max_key_num)):
        # defining key as random.choice from sequence of lowercase letter
        key = random.choice(string.ascii_lowercase)
        # defining value as random randint from 1 to 100
        value = random.randint(min_value, max_value)
        # adding new key:value pair into result
        result[key] = value
    # function returns dictionary result
    return result


# defining function that will create list of dictionaries
def create_list_dict(min_num_dict=2, max_num_dict=10) -> List[dict]:
    """This function creates list of dictionaries and accepts the following parameters:\n
    min_num_dict - minimum number of dictionaries inside the list, by default 2 \n
    max_num_dict - minimum number of dictionaries inside the list, by default 10
    """
    # defining blank list
    result_list = []
    # for loop to iterate random times (random.randint will choose random number n and in range (0,n) loop will work)
    for created_dict in range(random.randint(min_num_dict, max_num_dict)):
        # running create_dict() function and adding it into result_list
        result_list.append(create_dict())
    # returning result list
    return result_list

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# was added type hint from typing module to show that  takes list of dictionaries and returns dictionary


def create_common_dict(list_of_dicts: List[dict]) -> dict:
    """This function accepts new_list of dictionaries and returns one common dict:\n
    -  if dicts have same key, we will take max value, and rename key with dict number with max value\n
    -  if key is only in one dict - take it as is"""
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
    for i, d in enumerate(list_of_dicts, start=1):
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

    return result_dict


# running create_list_dict() function and assigning it to the new_list variable
new_list = create_list_dict()

# running create_common_dict() function and assigning it to the final_result variable
final_result = create_common_dict(new_list)
print(f"New dictionary HW2: {final_result}")

# HW3
# homEwork:
# 	tHis iz your homeWork, copy these Text to variable.
#
# 	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
#
# 	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
#
# 	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

# importing regular expressions module
import re


def convert_to_normalized_case(str_to_normalize: str) -> str:
    """This function accepts new_string and returns normalized from the case perspective string:"""
    # convert the source text to lowercase
    lower_source = str_to_normalize.lower()
    # define a regex pattern to split the text into sentences ('.','?' or '!' at the end of sentece,
    # followed whitespaces or new_line, followed by new word. i.e. end of every sentence
    pattern = r'([\.\?!]\s*)(\w+)'
    sentences = re.split(pattern, lower_source)
    # initialize a variable to store the normalized source text
    result = ""
    # capitalize the first letter of each sentence and append to normalized_source
    for sentence in sentences:
        result += sentence.capitalize()

    return result


def create_sentence_from_last_words(source_text: str) -> str:
    """This function accepts string text and returns new sentence from the last words of each sentence:"""
    # define a regex pattern to find the last word in each sentence
    pattern_last_word = r'(\s(\w+)[\.\?!])'

    # find the last words in each sentence and store them in new_words
    new_words = re.findall(pattern_last_word, source_text)

    # create a new line by joining the last words and capitalize it
    new_line = ''.join(word[1] + ' ' for word in new_words)
    new_line_cap = new_line.capitalize()

    return new_line_cap


def insert_text_into_text(source_text: str, pattern: str, new_line: str) -> str:
    """This function accepts source_text, new_line to input in the text and \n
     pattern of text  after which new_line should be added"""
    # find the index to insert the new line
    insert_index = source_text.find(pattern) + len(pattern)

    # split the text before and after the insertion point
    text_before_insert = source_text[:insert_index]
    text_after_insert = source_text[insert_index:]

    # insert the new line after the specified pattern
    new_text = text_before_insert + f' {new_line}' + text_after_insert

    return new_text


def str_find_replace(source_text: str, old_value: str, new_value: str) -> str:
    """This function accepts source_text the following parameters: \n
    - source_text: new text string where value will be changed from old_value to new_value
    - old_value: word that should be changed
    - new_value: word that will be inserted"""
    # replacing old_value to a new value in source_text
    new_text_replaced = re.sub(r"\b" + re.escape(old_value) + r"\b", new_value, source_text)
    return new_text_replaced


def calculate_spaces(source_text: str) -> int:
    """This function accepts text string  and returns number of all whitespace characters"""
    # calculate the number of all whitespace characters in the source_text
    space_count = len(re.findall(r'\s', source_text))
    return space_count


# assigning to a variable source string with the task
source = '''homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# functions test
# defining pattern after which we would insert new line
pattern_match = r'add it to the end of this paragraph.'

# normalized_text_with_added_sentence to get text with new sentence and right case
normalized_text_with_added_sentence = insert_text_into_text(convert_to_normalized_case(source), pattern_match, create_sentence_from_last_words(source))

# getting text with replaced iz to is
text_with_replaced_str = str_find_replace(normalized_text_with_added_sentence, 'iz', 'is')

# counting number of whitespaces
number_of_spaces = calculate_spaces(text_with_replaced_str)

# printing normalized text and the number of whitespace characters
print(f"Text with new line and normalized cases HW3:\n {text_with_replaced_str}")
print(f"Number of whitespaces HW3: {number_of_spaces}")
