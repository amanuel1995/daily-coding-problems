
# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def check(lst, k):
  i = len(lst)
  for stuff in lst:
    if(stuff + lst[i-1] == k):
      i -=1
      return True
    else:
      return False
      
print(check([10, 15, 3, 7], 17 ))
