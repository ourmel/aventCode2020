from helpers import read_text
import re

input_file = "input2"

list_str = read_text(input_file)
splitted_list = [re.split('-| ', x.replace(':', '')) for x in list_str]

valid = 0

for item in splitted_list:
    min_char = int(item[0])
    max_char = int(item[1])
    letter = item[2]
    body = item[3]

    if body.count(letter) >= min_char and body.count(letter) <= max_char:
        valid += 1

print(valid)

valid = 0
for item in splitted_list:
    first_pos = int(item[0]) - 1
    second_pos = int(item[1]) - 1
    letter = item[2]
    body = item[3]
    rule1 = 0
    rule2 = 0

    if body[first_pos] == letter:
        rule1 = 1
    if body[second_pos] == letter:
        rule2 = 1
    if rule1 + rule2 == 1:
        valid += 1

print(valid)