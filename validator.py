import re

strg = str(input())
pattern = r"(\d{8}1|8|9)"
ans = re.match(pattern ,strg)

if ans:
    print ("Valid number")
else:
    print ("Invalid number")