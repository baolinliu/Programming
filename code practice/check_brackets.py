___author__ = 'Baolin'

'''

This question has 2 parts:

Part 1:
    You are given a string which contains parentheses "()" and brackets "[]" 
    as well as other characters. e.g. "(12*(3+4)-dict['key'])"
    Your task is to write a function which determines whether or 
    not there are any problems with the usage of the parentheses and brackets.

Part 2:
    Given a string similar to that described in the 
    first part of the question and a location on that 
    string, return the location of the parenthesis or
    bracket that closes the first. e.g. "(12*(3+4))" 
    if given location 0 will return 9. If the location
    is not a parenthesis or bracket, it returns None. 
    If the parenthesis or bracket does not close, it 
    returns "Invalid use of parentheses/brackets"

'''

brackets = ['[','{','(',')','}',']']
closed = [")" ,"]" ,"}"]
opened = ["(","[" ,"{"]
pairs = ['{}','[]','()']


def bracket(string):
    '''
    Splits each inner bracket up
    Example ((()))() ---> [((())),()]
    '''
    string = list(string)
    for index in range(1,len(string)):
        if string[index-1] in closed and string[index] in opened:
            string.insert(index,'/')
    strings =''.join(string)
    strings = strings.split('/')
    return strings


def is_balanced(string):   
    for value in string:  # cleaning up the string so it will only have brackets, removes all else
        if value not in brackets:
            string = string.replace(value,"")
    

    strings = bracket(string)

    if type(strings) == str:
        strings = [strings]
        
    for string in strings:
    
        s = [string[index] for index in range(len(string)-1, -1, -1) if string[index] in closed]
        s1 = [string[index] for index in range(len(string)) if string[index] in opened]
        if len(s) != len(s1):
            return False
        else:
            return all([True if j+i in pairs else False for i,j in zip(s,s1)])
    
def first_bracket(string):  # in a for loop, as soon as you find an open bracket, you return the index
    for index,value in enumerate(string): 
        if value == "(" or value == "{" or value == "[":
            return index
    
    
def last_bracket(string):  # in a reverse for loop, as soon as you find an closed bracket, you return the index
    for index in range(len(string)-1, -1, -1): 
        if string[index] == ")" or string[index] == "]" or string[index] == "}":
            return index

def location(string):
    '''
    input: string
    output: index of the first open and close bracket
    '''
    if is_balanced(string) == False: # first check if this is possible from the previous function
        return "Invalid use of parentheses/brackets"
    else:
        b = bracket(string)[0]
        return first_bracket(b) , last_bracket(b)
    return None


print location("happy")
print location("(12*(3+4))")
print location("((})")
print location("{)")
print location("{)}")
print location("(cat)(dog)")
print location('(())(){}()[[]]')
print location('aaa()aaa')
print location('[](){}')



# Output:
# (None, None)
# (0, 9)
# Invalid use of parentheses/brackets
# Invalid use of parentheses/brackets
# Invalid use of parentheses/brackets
# (0, 4)
# (0, 3)
# (3, 4)
# (0, 1)

