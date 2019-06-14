Problem 1: Two Sums

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

1) Restate Question:
    So you want me to return two numbers on the list wthich add up to the
    target number.... No, you want me to return the indicies of the two
    numbers that addd up to the target number.

2) clarifying questions:
    Are the imputs intigers or floats or both?
    Should the output be a tuple or a list?

3) state assumptions.
  The inputs will be int
  relatively small list (under 20)
  output will be a list

  4) Process
    A) brainstorm:
        I could do a double for loop that will go through and see if the
        numbers add up to the target.

    B) This would be the quickest easiest way to get this done.

    c) But it is more of a brute force approach... Im sure there is a better Solution
    that would not be so time intensive. But for small lists it will work

    d)
