class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] postfix = new int[nums.length];

        // prefix
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                prefix[i] = nums[i];
            } else {
                prefix[i] = nums[i] * prefix[i - 1]; 
            }
        }

        // postfix
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i == nums.length - 1) {
                postfix[i] = nums[i];
            } else {
                postfix[i] = nums[i] * postfix[i + 1];
            }
        }

        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                res[i] = postfix[i + 1];
            } else if (i == nums.length - 1) {
                res[i] = prefix[i - 1];
            } else {
                res[i] = prefix[i - 1] * postfix[i + 1];
            }
        }

        return res;
    }
}