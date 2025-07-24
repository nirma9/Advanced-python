import re

# re.search()
txt = "python is powerful python"
# print(re.search("power",txt))
# print(re.findall("python",txt))

#re.sub(()
# txt = "phone: 98765-54321"
# print(re.sub(r"\d","*",txt))


print(re.match("python",txt))
print(re.match("powerful",txt))

#live demo pan card validation

import re
pan = "ABCDE 1 2 3 4 5 F"
pattern = r"^[A-Z]{5}[0-9]{4}[A-z]$"
if re.match(pattern,pan):
               print("valid pan card num....")
else:
        print('invalid pan number...')
