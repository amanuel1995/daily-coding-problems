
// ########################## Question Credits #####################################
// # founders@dailycodingproblem.com
// #################################################################################


/** 
 * ##################################################################################
 * Asked by : Uber
 * 
 * Given an array of ints, return a new array such that each element at index i 
 * of the new array is the product of all the numbers in the original array 
 * except the one at i.
 * 
 * For example, if our input was [1, 2, 3, 4, 5], 
 * the expected output would be [120, 60, 40, 30, 24]. 
 * If our input was [3, 2, 1], the expected output would be [2, 3, 6].
 * ##################################################################################
*/

class Solution {
    public static ArrayList<int> ProductMaker (int[] numsList) {
        ArrayList<int> resultArray =  new ArrayList<int> ();
        int multiple = 1;
        
        for (int i = 0; i < numsList.length; i++) {
            multiple = multiple * numsList[i];
        }

        for (int i = numsList.length; i<0; i-- ){
          resultArray.add(multiple / numsList[i]);
        }        
        return resultArray;
    }
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5};
        ArrayList<int> result = ProductMaker(nums);
        
        for (int num : result) {
            System.out.println(num);
        }

    }

}

/**
 * ##################################################################################
 * Problem extension ...
 * Bonus: What if you can't use division?
 * ##################################################################################
 */


// ################################# <NAME's> Solution ################################


// ################################## Test Case #1 ##################################

// ################################## Test Case #2 ##################################

// ################################## Test Case #3 ##################################

// ################################## Test Case #4 ##################################

// ################################## Test Case #5 ##################################

/**
 * Topics to review
 * Loops, Arrays and Arithmetic Operations
 */