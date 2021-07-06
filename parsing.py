

def removeExtraCharecters(text):
    output = ''
    for i in text:
        if i in ['0', '1','q', '\n', ' ']:
            output += i
    return output

def returnWithoutHash(lineOfText):
    output = ''
    for i in lineOfText:
        if i == '#':
            break
        output += i

    return output

def remove_end_charecters(code):
    i = -1
    while code[i] == ' ':
        i -= 1
    if i != -1:
        return code[0:i+1]
    return code

def parse(code):
    arrayOfCode = code.split('\n')
    tempArrayOfCode = []

    for line in arrayOfCode:
        if line != '' and line[0] != '#':
            #line = removeSpace(line)  # removing spaces in each line

            line = returnWithoutHash(line) # remove everything after "#" sign
            line = removeExtraCharecters(line) # removing every charecter that is not one of the 8 main charecters
            line = remove_end_charecters(line)


            tempArrayOfCode.append(line + '\n')   # the last two lines: destroying lines with nothing on them(filtering them by sending the ones with things on them into another list)


    arrayOfCode = tempArrayOfCode
    return "".join(arrayOfCode)


