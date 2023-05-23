import re

strings = ['04', '054', '972', '972-45', '72-054', '777777', '054555555', '054-778855', '972-45-778855', '972-45-778855']

pat = '(\d{2,3}-?)?(0\d{1,2}-?)?(\d{7})$'

for string in strings:
    res = re.findall(pat, string)
    print(res)

    match = re.search(pat, string)
    print("match: "+str(match))

stringToSplit = "hello im 12 yo in 2 days"
pat2 = "[0-9]+"
result = re.split(pat2, stringToSplit)
print(result)

stringTomatch = "123&^*()asd"
pat3 = "[A-Z]"
isMatch = re.match(pat3, stringTomatch)
print(isMatch)