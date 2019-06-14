#! /bin/python3


def twoSum(nums, target):
    #run double for loop to find a combo of numbers to get to Target
    for i in range(0, (len(nums)-1)):
        for x in range((i+1), (len(nums)-1)):
            if nums[i]+ nums[x] == target:
                return [i, x]

#test
if __name__ == "__main__":
    list_a=[1, 3, 4, 5, 6, 8, 10]
    target = 9
    result = twoSum(list_a, target)
    print(result)
    if result == [2, 3]:
        print(True)
    else:
        print(False)
