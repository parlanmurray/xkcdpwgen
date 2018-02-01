#!/usr/bin/python3

from random import randint
import sys, getopt

words = 4
caps = 0
numbers = 0
symbols = 0
special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "<", ">", "?", "~"]

try:
    opts, args = getopt.getopt(sys.argv[1:], "hc:w:n:s:", ["help", "caps=", "words=", "numbers=",
                                                           "symbols="])
except getopt.GetoptError:
    print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]")
    sys.exit(2)
for opt, arg in opts:
    if opt in ('-h', "--help"):
        print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\n" +
              "Generate a secure, memorable password using the XKCD method\n\n" +
              "optional arguments:\n" +
              "    -h, --help            show this help message and exit\n" +
              "    -w WORDS, --words WORDS\n" +
              "                          include WORDS words in the password (default=4)\n" +
              "    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n" +
              "                          (default=0)\n" +
              "    -n NUMBERS, --numbers NUMBERS\n" +
              "                          insert NUMBERS random numbers in the password\n" +
              "                          (default=0)\n" +
              "    -s SYMBOLS, --symbols SYMBOLS\n" +
              "                          insert SYMBOLS random symbols in the password\n" +
              "                          (default=0)")
        sys.exit()
    elif opt in ("-w", "--words"):
        words = int(arg)
    elif opt in ["-c", "--caps"]:
        caps = int(arg)
    elif opt in ["-n", "--numbers"]:
        numbers = int(arg)
    elif opt in ["-s", "--symbols"]:
        symbols = int(arg)

with open('corncob_lowercase.txt') as f:
    lines = f.read().splitlines()

pwd = ''
for i1 in range(words):
    x = randint(0, len(lines) - 1)
    temp = lines[x]
    if caps >= (words - i1):
        temp = temp[0].upper() + temp[1:]
    elif caps > 0:
        if randint(0, words) < caps:
            temp = temp[0].upper() + temp[1:]
            caps -= 1
    pwd += temp

for i2 in range(numbers):
    x = randint(0, len(pwd) - 1)
    pwd = pwd[0:x] + str(randint(0, 9)) + pwd[x:]

for i3 in range(symbols):
    x = randint(0, len(pwd) - 1)
    pwd = pwd[0:x] + special[randint(0, len(special) - 1)] + pwd[x:]

print(pwd)
