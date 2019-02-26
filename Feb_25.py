###############################################################################
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.
###############################################################################

########################## Question Credits ###################################
# founders@dailycodingproblem.com
###############################################################################


################################# My Solution #################################
def missing_number( arry):
    
    # smallest positive integer
    # all positive --> 1 or smallest
        # if 1 or smallest is in arry
        # increment by 1
    # all negative --> 1
    
    if len(arry) != 0:
        smallest_positive = arry[0]
        for n in (arry):
            # get the min {either the smallest in the list or 1}
            if(n < smallest_positive and n > 0):
                smallest_positive = n
            elif (n < 1):
                smallest_positive = 1
        if smallest_positive > 1:
            smallest_positive = 1
        else:
            while smallest_positive in arry:
                smallest_positive += 1
    else:
        return 1

    return smallest_positive 


################################## Test Case ##################################
print(missing_number([ 2, 3, 77, 30]), "Should be 1")
print(missing_number([1, 2, 3, 7, 30]), "Should be 4")
print(missing_number([2, 0, 5, 10]), "Should be 1")
print(missing_number([122, 0, 5, 10]), "Should be 1")
print(missing_number([-1, 0, 15, 10]), "Should be 1")
print(missing_number([-3, 4, -1, 1]), "Should be 2")
print(missing_number([-3, 4, -1, 1, 2, 3, -4]), "Should be 5")
print(missing_number([-4, 1, 2, 3, 4, 5]), "Should be 6")
print(missing_number([2]), "Should be 1")
print(missing_number([]), "Should be 1")
print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, -1, 11, -2]), "Should be 9")
################################## Test Case ##################################


# Problem extension
# Bonus: optimize better for linear time and constant space.
#...
