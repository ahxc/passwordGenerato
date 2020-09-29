import random, sys, os
from functools import reduce

numberS = "0123456789"
characterS = "!@#$%^&*.+=?_"
lowerS = "abcdefghijklmnopqrstuvwxyz"
choice = numberS + characterS + lowerS + lowerS.upper()
def joinS(a, b):
	return a+b

passwordName = sys.argv[1]
passwordNumber = sys.argv[2]
if len(sys.argv) >= 4:
	passwordPath = os.path.join(sys.argv[3], "password.txt")
else:
	passwordPath = "password.txt"
password = reduce(joinS, random.sample(choice, int(passwordNumber)))
password = passwordName + "：" + password

with open(passwordPath, 'a', encoding="utf-8") as f:
	f.write(password + '\n')