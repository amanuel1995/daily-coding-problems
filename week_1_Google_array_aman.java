// ########################## Question Credits #####################################
// # founders@dailycodingproblem.com
// #################################################################################


/** 
 * ##################################################################################
 * Given an array of numbers and a number k, return whether any two numbers 
 * from the array add up to k.
 * For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
 * ##################################################################################
*/

/**
 * ##################################################################################
 * Problem extension ...
 * Bonus: Can you do this in one pass i.e using only one loop?
 * ##################################################################################
 */


// ################################# Aman's Solution ################################
public class Solution{
  public static void SumFinder(Integer[] numbers, Integer k) {
    Integer[] numList = numbers;
    
    for (int i =0; i < numbers.length; i++){
      System.out(i);
    }
    
  public static main(String[] args){
    Integer[] array1 = {10,15,3,7};
    Integer k1 = 17, k2 = 15, k3 = 13, k4 =25, k5 = 100;
   
    // ################################## Test Case #1 ##################################
    Solution.SumFinder(array1, k1);
  }

  }  
}


// ################################## Test Case #2 ##################################

// ################################## Test Case #3 ##################################

// ################################## Test Case #4 ##################################

// ################################## Test Case #5 ##################################

/**
 * Topics to review
 * Loops, Arrays and Array Operations
 */