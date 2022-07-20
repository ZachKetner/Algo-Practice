from pickle import TRUE


def reverseArray(arrayInput):
    for i in range(int(len(arrayInput)/2)):
        temp = arrayInput[i] # temp varible keeping track of arrayInput's value at position 1
        arrayInput[i] = arrayInput[len(arrayInput)-1-i]
        arrayInput[len(arrayInput)-1-i] = temp
        if i == len(arrayInput)/2:
            return arrayInput
    return arrayInput

print(reverseArray([3,2,1,4,5]))

# String Algos
#   - Parens/brackets/curly brackets Valid Valid sets of parentheses always open
#     before they close, for example. For "Y(3(p)p(3)r)s", return true. Given
#     "N(0(p)3", return false: not every parenthesis is closed. Given "N(0)t
#     )0(k", return false, because the underlined ")" is premature: there is
#     nothing open for it to close.

def ValidParens(string):
    openParen = 0
    closeParen = 0
    for paren in range(len(string)):
        if string[paren] == '(':
            openParen += 1
        elif string[paren] == ')':
            closeParen += 1
        print(openParen)
        print(closeParen)
        if closeParen > openParen:
            return False
    if closeParen != openParen:
        return False
    return True
            

print(ValidParens("Y(3(p)p(3)r)s"))