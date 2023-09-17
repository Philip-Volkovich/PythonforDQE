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


# assigning to a variable source string with the task
source = '''homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# Convert the source text to lowercase
lower_source = source.lower()

# Define a regex pattern to split the text into sentences ('.','?' or '!' at the end of sentece, followed whitespaces
# or new_line, followed by new word. i.e. end of every sentence
pattern = r'([\.\?!]\s*)(\w+)'
sentences = re.split(pattern, lower_source)

# Initialize a variable to store the normalized source text
normalized_source = ""

# Capitalize the first letter of each sentence and append to normalized_source
for sentence in sentences:
    normalized_source += sentence.capitalize()

# Count the number of whitespace characters in the original source text
space_count_initial = len(re.findall(r'\s', source))

# Define a regex pattern to find the last word in each sentence
pattern_last_word = r'(\s(\w+)[\.\?!])'

# Find the last words in each sentence and store them in new_words
new_words = re.findall(pattern_last_word, normalized_source)

# Create a new line by joining the last words and capitalize it
new_line = ''.join(word[1] + ' ' for word in new_words)
new_line_cap = new_line.capitalize()

# Define a pattern to find the position to insert the new line
par_pattern = r'add it to the end of this paragraph.'

# Find the index to insert the new line
insert_index = normalized_source.find(par_pattern) + len(par_pattern)

# Split the text before and after the insertion point
text_before_insert = normalized_source[:insert_index]
text_after_insert = normalized_source[insert_index:]

# Insert the new line after the specified pattern
new_text = text_before_insert + f' {new_line_cap}' + text_after_insert

# Replace "iz" with "is" where it is necessary
new_text_iz_fixed = re.sub(r'\b(iz)\b', 'is', new_text)

# Calculate the number of all whitespace characters in the modified text
space_count = len(re.findall(r'\s', new_text_iz_fixed))

# Printing normalized text and the number of whitespace characters
print(f"Text with new line and normalized cases:\n {new_text_iz_fixed}")
print(f"Number of whitespaces: {space_count}")
