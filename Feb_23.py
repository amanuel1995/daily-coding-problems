###############################################################################
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is
# the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
###############################################################################

########################## Question Credits ###################################
# founders@dailycodingproblem.com
###############################################################################


################################# My Solution #################################
def product_arrays(lst):
    result = []

    products = 1
    i = 0 
    for each_num in lst:
        products  *= each_num
        i += 1
    

    j =0 
    
    while j < len(lst):
        result.append( products/lst[j])
        j += 1

    return result

print(product_arrays([1, 5, 10]))


# Problem extension
# Bonus: what if you can't use division?
#...
