package trial.code.leet.arrays;

// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

import java.util.*;

public class FindDisappearedNumbers {
    public static void main(String[] args) {
        int[] value = new int[]{4,3,2,7,7,2,3,1};
        System.out.println(findDisappearedNumbers(value));
    }

    public static List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> result = new ArrayList<>();
        for(int i=0; i<nums.length; i++) {
            if((i+1) == nums[i]) {
                if(result.contains(i+1)) {
                    result.remove((Integer) (i+1));
                }
                continue;
            }
            else if(result.contains(nums[i]) || (i+1) > nums[i]){
                result.remove((Integer) nums[i]);
            } else {
                result.add(nums[i]);
            }
            if(result.contains(i+1)) {
                result.remove((Integer) (i+1));
            } else {
                result.add(i+1);
            }
        }
        return result;
    }
}
