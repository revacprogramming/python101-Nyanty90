# Regular Expressions
# https://www.py4e.com/lessons/regex

import re
print(sum([int(i) for i in re.findall("[0-9]+", open("./py-101/dataset/regex_sum_1550751.txt", "r").read())]))
