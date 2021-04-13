import string
import sys
p = sys.argv[1]
s = 0
for c in p:
    if c in string.ascii_uppercase:
        s += 2
    elif c in string.ascii_lowercase:
        s += 1
    elif c in "0123456789":
        s += 3
    elif c in " !#$%&()=":
        s += 3
print(s)
