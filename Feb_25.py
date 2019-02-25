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
    # all positive --> sorted() index 0 -1, if that number is not zero
    # all negative --> 1
    # mixed 

    sorted_arry = sorted(arry)
    smallest_positive = 1000000000000000

    for n in (sorted_arry):
        if(n < smallest_positive and n > 0):
            smallest_positive = n
    
    while (True):
        if(smallest_positive - 1 !=0 and smallest_positive-1 not in sorted_arry):
            smallest_positive -= 1
            break 
        elif (smallest_positive -1 == 0):
            smallest_positive += 1
            
        if(smallest_positive in sorted_arry):
            smallest_positive += 1
        else:
            return smallest_positive
    
    return smallest_positive 

################################## Test Case ##################################
print(missing_number([1, 2, 3, 7, 30]))
print(missing_number([2,0, 5, 10]))
print(missing_number([122,0, 5, 10]))
print(missing_number([-1,0, 15, 10]))
################################## Test Case ##################################


# Problem extension
# Bonus: 
#...
