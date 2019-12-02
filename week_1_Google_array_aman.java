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

// ################################# Amanuel's Solution #############################
class Main {  

    // method to find if k is sum of any two numbers
    public static boolean SumFinder(Integer[] numbers, Integer k) {
      boolean flag = false;
      
      // runtime of N squared.
      for (int i =0; i < numbers.length; i++){
        for (int j=0; j< numbers.length; j++){
          if (numbers[i] + numbers[j] == k){
            if (j != i){
              flag = true;
            }
          }
        }
      }
  
      return flag;
    }

    /**
     * ##################################################################################
     * Problem extension ...
     * Bonus: Can you do this in one pass i.e using only one loop?
     * ##################################################################################
     */

    public static boolean LinearSolutionSumFinder(Integer[] numbersList, Integer K ) {
        boolean flag = false;

        return flag;
        
    }

  
    public static void main(String[] args) {
      Integer[] myArry = {10, 15, 3, 7};
      
      // First Solution Tests
      // ################################## Test Case #1 ##################################
      int k1 = 17;
      boolean test1 = SumFinder(myArry, k1);
      System.out.println(test1);
      // ################################## Test Case #2 ##################################
      int k2 = 28;
      boolean test2 = SumFinder(myArry, k2);
      System.out.println(test2);
      // ################################## Test Case #3 ##################################
      int k3 = 10;
      boolean test3 = SumFinder(myArry, k3);
      System.out.println(test3);
      // ################################## Test Case #4 ##################################
      int k4 = 6;
      boolean test4 = SumFinder(myArry, k4);
      System.out.println(test4);
      // ################################## Test Case #5 ##################################
      int k5 = 13;
      boolean test5 = SumFinder(myArry, k5);
      System.out.println(test5);

      // Linear Algorithmic Time Solution - Tests
      // ################################## Test Case #1 ##################################

      // ################################## Test Case #2 ##################################

      // ################################## Test Case #3 ##################################
      
      // ################################## Test Case #4 ##################################

      // ################################## Test Case #5 ##################################

    }
    
  }
/**
* Topics to review
* Loops, Arrays and Array Operations
*/