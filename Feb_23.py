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

    # multiply every array member divide the product at index i by the excluded index from the initial array 
    
    for each_num in lst:
        products  *= each_num
    
    # int_result = [result.append(int(products/lst[i])) for i in lst]
    for n in range(len(lst)):
        try:
            result.append( int(products/lst[n])) 
        except ZeroDivisionError:
            result.append(0)
            # print("Zero Division Error")   
    
    return result


################################## Test Case ##################################
print(product_arrays([1, 5, 10]))
print(product_arrays([1, 2, 3, 4, 5]))
print(product_arrays([3, 2, 1]))
print(product_arrays([0, 5, 10])) # FAIL
print(product_arrays([2, 4, 2]))
print(product_arrays([10, 20, 30]))
print(product_arrays([5, 10]))
print(product_arrays([100,200,300,400]))
################################## Test Case ##################################


# Problem extension
# Bonus: what if you can't use division?
#...

