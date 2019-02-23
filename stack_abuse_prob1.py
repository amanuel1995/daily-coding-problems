
# Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def check(lst, k):
    index = 0
    lstsize = len(lst)
    
    while (index < lstsize):
        for the_num in lst:
            if ((the_num + lst[index] == k) and (the_num != lst[index])):
                return True
        index += 1
    
    return False

############## Test Cases ############
print(check([10, 15, 3, 7], 17))
print(check([1, 5, 6], 11))
print(check([1, 5, 6, 1], 12))
print(check([1, 5, 6, 1], 6))
print(check([1, 5, 6, 2], 7))
print(check([1, 5, 6, 8], 4))
############## Test Cases ############

# Problem extension
# Bonus: Can you do this in one pass?
#...

