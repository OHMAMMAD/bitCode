


def bi2BCD(bi):
    bi = str(bi)
    output = 0

    i = -1
    while i >= len(bi) * -1:
        dig = bi[i]

        if dig == '1':
            output += 2 ** (i * -1 - 1)

        i -= 1
    return output


def joinListElements(theList):
	output = ''
	for i in theList:
		output += i
	return output

def BCD2bi(dec):
    numBefore = 0
    num = 0
    i = 0
    output = ['0', '0', '0', '0']

    while dec > 0:

        if num >= dec and dec > numBefore:

            if len(output) < i:  # if list too small
                for times in range(i - len(output)):
                    output.append('0')

            if num == dec:
                output[i * -1] = '1'
                dec -= num
            else:
                output[(i-1) * -1] = '1'
                dec -= numBefore

            if output[0] == '0' and len(output) > 4:
                output.append('0')
                output = output[1:-1]

            i = 0
            num = 0
            numBefore = 0

        numBefore = num
        num = 2 ** i
        i += 1

    return "".join(output)

