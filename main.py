

from binary import *
from parsing import *
from alu import Alu
import time


registers = ['0', '0', '0', '0']

alu = Alu()

accessDis = '0000'

insert = '0000'

isAluSet = False



def make_list(lst):
    output = []
    for i in lst:
        output.append(i.split(' '))
    return output



file = open('code_eg2.txt', 'r')
code = file.read()
file.close()

print(code)
code = parse(code)

print(code)

code = code.split('\n')
code = code[0:-1]
print(code)

lenCode = len(code)

code = make_list(code)

line = 0
while line < lenCode:

    for command in range(len(code[line])):
        cm = code[line][command]

        if command == 0 and cm == '1001':
            insert = code[line][2]
        if command == 0 and cm == '0011':
            registers[bi2BCD(code[line][2]) - 1] = accessDis
            insert = '0000'
        if command == 0 and cm == '1100':
            if code[line][1] == '1':
                #if alu.retAb()[0] != '0000':
                alu.setA(registers[bi2BCD(code[line][2]) - 1])
            else:
                alu.setB(registers[bi2BCD(code[line][2]) - 1])
        if command == 0 and cm == '1010':
            if code[line][1] == '0':
                if registers[3] == '0000':
                    command = 0
                    line = bi2BCD(code[line][2]) - 1  # imp
            else:
                if bi2BCD(registers[3]) > 0:
                    command = 0
                    line = line = bi2BCD(code[line][2]) - 1
        if command == 0 and cm == '0110':
            alu.toggle_mode()

    accessDis = alu.output()
    if insert != '0000':
        accessDis = insert

    time.sleep(.5)

    print(f'{" ".join(code[line])}       {accessDis}    {registers}         {alu.retAb()}')
    line += 1

