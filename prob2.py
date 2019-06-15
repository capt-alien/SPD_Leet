#! /bin/python3
# class Solution:
#     def isValid(self, string):
#         listify = string.split()
#         return listify
def isValid(string):
    listify = list(string)
    stacka = []
    for char in listify:
        if char == '(' or char == '[' or char == '{':
            stacka.append(char)
        #Chek the last entry in stack to see if it matches
        if char == ')' or char == ']' or char == '}':
            #check last entry in stack
            peak = stacka[len(stacka)-1]
            if peak == '(' and char == ')':
                stacka.pop()
            elif peak == '{' and char == '}':
                stacka.pop()
            elif peak == '[' and char == ']':
                stacka.pop()
            else:
                return False
    #Return true if nothing left in stacka
    if len(stacka) == 0:
        return True
    else:
        return False


#test
if __name__ == "__main__":

    test_a = '({[]})'
    test_b = '({)}[{]}'
    test_c = '{)[}(}'
    print(isValid(test_a))
    print(isValid(test_b))
    print(isValid(test_c))
