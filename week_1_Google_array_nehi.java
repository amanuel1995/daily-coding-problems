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


// ################################# Nehemiah's Solution ################################
	static boolean addsUpToK(int[] a, int k) {
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a.length; j++) {
				if (a[i] + a[j] == k && i != j) {
					return true;
				}
			}
		}
		return false;
	}

// inputs
	int[] a = {10, 15, 3, 7};

// ################################## Test Case #1 ##################################
	addsUpToK(a, 17); // => true
// ################################## Test Case #2 ##################################
	addsUpToK(a, 0); // => false
// ################################## Test Case #3 ##################################
	addsUpToK(a, -13); // => false
// ################################## Test Case #4 ##################################
	addsUpToK(a, 20); // => false
// ################################## Test Case #5 ##################################
	addsUpToK(a, 10); // => true
/**
 * Topics to review
 * Loops, Arrays and Array Operations
 */