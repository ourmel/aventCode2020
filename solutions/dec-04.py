import os
import re


# #
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def isByrOk(byr_val):
    try:
        if int(byr_val) >= 1920 and int(byr_val) <= 2002:
            return True
        else:
            return False
    except NameError:
        return False


# iyr (Issue Year) - four digits; at least 2010 and at most 2020.

def isIyrOk(iyr_val):
    try:
        if int(iyr_val) >= 2010 and int(iyr_val) <= 2020:
            return True
        else:
            return False
    except NameError:
        return False


# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

def isEyrOk(eyr_val):
    try:
        if int(eyr_val) >= 2020 and int(eyr_val) <= 2030:
            return True
        else:
            return False
    except NameError:
        return False


# hgt (Height) - a number followed by either cm or in:

def isHeightOk(hgt):
    if len(hgt) < 3:
        return False
    hgt_units = hgt[-2:]
    hgt_val = hgt[:-2]
    if hgt_units not in ['cm', 'in']:
        return False
    try:
        hgt_val = int(hgt_val)
        if hgt_units == 'cm':
            return 150 <= hgt_val <= 193
        if hgt_units == 'in':
            return 59 <= hgt_val <= 76
        return True
    except NameError:
        return False


# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def isHclOk(hcl):
    if hcl[0] != '#':
        return False
    if len(hcl[1::]) != 6:
        return False
    for l in hcl[1:]:
        if not (ord('a') <= ord(l) <= ord('f')) and not (ord('0') <= ord(l) <= ord('9')):
            return False
    return True


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def isEclOk(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False


# pid (Passport ID) - a nine-digit number, including leading zeroes.
def isPidOk(pid):
    if len(pid) == 9:
        try:
            int(pid)
            return True
        except NameError:
            return False
    else :
        return False


# cid (Country ID) - ignored, missing or not.

day = 4
filename = str('input' + str(day))
print(os.listdir())

file1 = open(str('input/' + filename + '.txt'), 'r')
raw_passport = file1.read().split('\n\n')
clean_passport_list = [x.split() for x in raw_passport]

mandatoryKeys = ["pid", "eyr", "ecl", "hgt", "iyr", "byr", "hcl"]
optionalKey = ["cid"]

passport_dict = {}
valid_count = 0
for passport, i in zip(clean_passport_list, range(0, len(clean_passport_list))):
    dict_pass = {}
    for entry in passport:
        key, value = entry.split(':')
        dict_pass[key] = value
    if all(elem in dict_pass.keys() for elem in mandatoryKeys):
        if isHeightOk(dict_pass['hgt']) and \
                isByrOk(dict_pass['byr']) and \
                isEclOk(dict_pass['ecl']) and \
                isEyrOk(dict_pass['eyr']) and \
                isIyrOk(dict_pass['iyr']) and \
                isHclOk(dict_pass['hcl']) and \
                isPidOk(dict_pass['pid']):
            valid_count += 1

# passport_dict[i] = dict_pass

print(valid_count)

