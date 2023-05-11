str = input()
new_str = ''
for s in str:
    if ord(s)<=90:
        new_str += s.lower()
    else:
        new_str += s.upper()
print(new_str)