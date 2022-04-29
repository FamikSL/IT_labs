import string
import sys
import os
import os.path


def is_file_exist(filename):
    return (os.path.isfile(filename))

def create_file(filename, text, method):
        try:
            with open(filename, method) as file_handler:
                file_handler.write(text)
        except IOError:
            print("An IOError has occurred!")
            
params = (sys.argv)

if len(params) == 1:
    sys.exit('no pid')
try:
    params[1] = int(params[1])
except:
    sys.exit('bad pid')

to_file = False

if len(params) == 3:
    to_file = True
    filename = params[2]

given_pid = sys.argv[1]
if to_file:
    text = os.popen(cmd=f'pmap {given_pid}').read()
    if is_file_exist(filename):
        ans=''
        print("File with this name is already exist.\n", end='')
        while True:
            print("Type R to overwriting the file. Type N to reaname file.\n", end='')
            ans = input()
            if ans == "R" or ans == "N":
                break
        if ans == "R":
            create_file(filename, text, 'w+')
        else:
            print("Type new filename\n", end='')
            new_filename = ans = input()
            create_file(new_filename, text, 'w')
        
    else:
        create_file(filename, text, 'w')
else:
    os.system(f'pmap {given_pid}')
