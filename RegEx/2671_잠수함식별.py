import re

str = input()
t = re.compile("(100+1+|01)+")
if t.fullmatch(str):
    print("SUBMARINE")
else:
    print("NOISE")
