#! /bin/python3
# class Solution:
#     def isValid(self, string):
#         listify = string.split()
#         return listify
def isValid(string):
    listify = list(string)
    stacka= []
    for char in listify:
        if char == '(' or char == '[' or char == '{':
            stacka.append(char)
        #Chek the last entry in stack to see if it matches
        if char == ')' or char == ']' or char == '}':
            #return false if len()
            check = listify[len(listify)-1]
            if check == '(' and char == ')':
                listify.pop()
            elif check == '{' and char == '}':
                listify.pop()
            elif check == '[' and char == ']':
                listify.pop()
            else:
                return False
    #Return true if nothing left in stacka
    if len(stacka) == 0:
        return True
    else:
        return False








#test
if __name__ == "__main__":

    test_a = '(({[{[]}]()}{}){})'
    test_b = '({)}[{]}'
    test_c = '{)[}(}'
    print(test_a)
    print(isValid(test_a))
