# Array-5

## Problem1: Bind Robot in a Circle (https://leetcode.com/problems/robot-bounded-in-circle/)


## Problem2: Calculate Tax

 Write a program to calculate tax if Salary and Tax Brackets are given as list in the form [ [10000, .3],[20000, .2], [30000, .1], [None, .1]]. You don’t know in the beginning how many tax brackets are there. You have to test for all of them 
 
 class GFG {

	public static void main (String[] args) {

		List<List<Double>> levels = new ArrayList<>();

        levels.add( Arrays.asList(10000.0, 0.3) );

        levels.add( Arrays.asList(20000.0, 0.2) );

        levels.add( Arrays.asList(30000.0, 0.1) );

        levels.add( Arrays.asList(null, 0.1) );

        double tax = calculateTax(levels,45000);

        System.out.println(tax);

	}

	public static double calculateTax(List<List<Double>> levels, double salary ){


    }

}
