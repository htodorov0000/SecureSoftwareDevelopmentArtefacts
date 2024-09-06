import re

pattern = r"[A-Z][A-Z0-9]{0,3} [0-9][A-Z]{2}"

while True:
    post_code_entry = input("Enter a UK postcode.")
    find = re.findall(pattern, post_code_entry)
    if len(find) == 1:
        if find[0] == post_code_entry:
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Wrong!")