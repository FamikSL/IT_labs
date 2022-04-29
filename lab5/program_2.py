from re import T
import getch
import sys
import os
import os.path
from time import sleep


def symbol_output(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
def symbol_input():
    i = 1
    string = ''
    char = sys.stdin.read(i)
    
    while char != "\n":
        i+=1
        string += char
        char = sys.stdin.read(i)
        
    return string

def is_file_exist(filename):
    return (os.path.isfile(filename))

params = sys.argv

if len(params) == 1:
    sys.exit('no filename')

if len(params) > 1:
    filename = params[1]

N=0
if len(params) == 3:
    N = int(sys.argv[2])

if not is_file_exist(filename):
    sys.exit('There is no such file')

try:
    with open(filename, 'r') as file_handler:
            text = file_handler.readlines()
except IOError:
    print("An IOError has occurred!")

if N == 0:
    for line in text:
        symbol_output(line)
    sys.exit()
else:
    text = text[::-1]
    for i in range(len(text)-1, len(text)-1-N, -1):
        print(text[i], end='')
        text.pop(i)

text = text[::-1]

char = getch.getch()
count = 0
for i in range(len(text)):

    if count ==N:
        char = getch.getch()

        count = 0
    symbol_output(text[i])
    count +=1
 
