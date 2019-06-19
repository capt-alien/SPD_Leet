#! user/bin/python

def got_dup(list):
    """given a list of n numbers determine
    if it contains a duplicate number"""
    a = len(list)
    bset = set(list)
    if a == len(bset):
        return True
    else:
        return False

if __name__ == '__main__':
    list_a = [1,3,4,6,7,89,8,9,3,4,5,11]
    list_b = [1,2,3,4,5,6,7,8,9,10]
    print(got_dup(list_a))
    print(got_dup(list_b))
