class Solution {
    public void moveZeroes(int[] nums) {
        int slow = 0;

        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0 && nums[slow] == 0) {
                // switch slow and fast ptr
                int temp = nums[slow];
                nums[slow] = nums[fast];
                nums[fast] = temp;
            }

            if (nums[slow] != 0) {
                slow++;
            }
            // System.out.println(Arrays.toString(nums));
        }

    }
}