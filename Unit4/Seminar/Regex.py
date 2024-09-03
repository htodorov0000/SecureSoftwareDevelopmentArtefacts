import re

post_code = "SW1A 2AA"

pattern = r"[A-Z][A-Z0-9]{0,3} [0-9][A-Z]{2}"

test = "ST7 9HV"

find = re.findall(pattern, test)
print(find)