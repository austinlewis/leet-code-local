package trial.code.leet.arrays;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/contains-duplicate/

public class ContainsDuplicate {
    public static void main(String[] args) {
        int[] value = new int[]{-1, -2, -3, 1, 2, 3, -1, 4};
        System.out.println(containsDuplicate(value));
    }

    public static boolean containsDuplicate(int[] nums) {
        /* using Arrays.stream
        Leetcode Submission - https://leetcode.com/submissions/detail/527707931/
        Runtime: 7 ms
        Memory Usage: 46.4 MB */

        // return Arrays.stream(nums).distinct().count() != nums.length;

        /* using forEach
        Leetcode Submission - https://leetcode.com/submissions/detail/527712796/
        Runtime: 4 ms
        Memory Usage: 42.8 MB */

        Set<Integer> uniqueValues = new HashSet<Integer>();
        for (int num : nums) {
            if (!uniqueValues.add(num)) {
                return true;
            }
        }

        //TODO: Why does the forEach method take less runtime compared to in-built Arrays.stream(); Is it because of the distinct(), if so how much and why?

        return false;
    }
}
