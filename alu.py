

from binary import *

class Alu:
    def __init__(self):
        self.abL = ['0000', '0000']
        self.abLSplit = [self.spl(self.abL[0]), self.spl(self.abL[1])]
        self.mode = 'sum'
        print(self.abLSplit)
    def spl(self, inp):
        output = []
        for i in range(len(inp)):
            output.append(inp[i])
        return output

    def update_abL(self):
        self.abL[0] = "".join(self.abLSplit[0])
        self.abL[1] = "".join(self.abLSplit[1])
    def update_abLSplit(self):
        self.abLSplit[0] = self.spl(self.abL[0])
        self.abLSplit[1] = self.spl(self.abL[1])
    def invert_b(self):
        b = self.abLSplit[1]
        for dig in range(len(b)):
            if b[dig] == '1':
                b[dig] = '0'
            else:
                if b[dig] == '0':
                    b[dig] = '1'
        self.abLSplit[1] = b
        self.update_abL()
    def calcSum(self):
        output = BCD2bi(bi2BCD(self.abL[0]) + bi2BCD(self.abL[1])) + '0'
        return output[len(output)-1 - 4:-1]

    def calcSub(self):
        output = BCD2bi(bi2BCD(self.abL[0]) - bi2BCD(self.abL[1])) + '0'
        return output[len(output)-1 - 4:-1]
    def setAb(self, a, b):
        self.abL[0], self.abL[1] = a, b
        self.update_abLSplit()
    def setA(self, a):
        self.abL[0] = a
        self.update_abLSplit()

    def setB(self, b):
        self.abL[1] = b
        self.update_abLSplit()

    def retAb(self):
        return self.abL

    def Or(self):
        output = ''
        for i in range(len(self.abL[0])):
            numAdding = '0'
            if self.abL[0][i] == '1' or self.abL[1][i] == '1':
                numAdding = '1'
            output += numAdding
        return output
    def toggle_mode(self):
        if self.mode == 'sum':
            self.mode = 'sub'
        else:
            self.mode = 'sum'
    def output(self):
        if self.mode == 'sum':
            return self.calcSum()
        if self.mode == 'sub':
            return self.calcSub()
