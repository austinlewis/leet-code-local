package trial.code.leet.arrays;

import java.util.Arrays;

// https://leetcode.com/problems/missing-number/
public class MissingNumber {

    public static void main(String[] args) {
        int[] value = new int[]{2,1};
        System.out.println(missingNumber(value));
    }

    public static int missingNumber(int[] nums) {
        /* using Arrays.stream
        Leetcode submission - https://leetcode.com/submissions/detail/527966122/
        Runtime: 2 ms
        Memory Usage: 38.9 MB */

        int currentSum = Arrays.stream(nums).sum();
        for(int i=0; i<=nums.length; i++) {
            currentSum = currentSum - i;
        }
        return currentSum*-1;

        /* TODO: Try without Arrays.stream using for-loop
        int sum = 0;
        for(int i=0; i<nums.length; i++) {
            System.out.println(nums[i]);
            System.out.println(i);
            sum = sum + 1 - nums[i];
        }

        return sum;

         */
    }
}
