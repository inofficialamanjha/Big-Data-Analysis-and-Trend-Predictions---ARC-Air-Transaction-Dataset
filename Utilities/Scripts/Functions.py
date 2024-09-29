import re
from datetime import datetime


def IncreaseDictValue(dictionary, key):
    if key in dictionary:
        dictionary[key] = dictionary[key] + 1
    else:
        dictionary[key] = 1

    return dictionary


def isNan(num):
    return num != num


def convertStringToDateTime(string):
    match = re.search("\d\d\d\d-\d\d-\d\d", string)
    return datetime.strptime(match.group(), '%Y-%m-%d')
    # (x-y).days
