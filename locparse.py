# My Project1999 Log Parser

import re               # Regular Expressions Module
import os
import time

# Configure the eq log path
filepath = 'logsample.txt'

# Read the log file line by line
# Load the contents into a LIST
with open(filepath) as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# 
def is_word_in_text(word, text):
    pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
    pattern = re.compile(pattern, re.IGNORECASE)
    matches = re.search(pattern, text)
    return bool(matches)

#print (content)
# Loop through the list and get the last Location
for cntr, value in enumerate(content, 1):
    if (is_word_in_text('Location',value)):
        #print (value)
        myindex = cntr-1

# Format the numbers
print (content[myindex].split(']')[1].lstrip())