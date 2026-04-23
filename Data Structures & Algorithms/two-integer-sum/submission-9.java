class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++)
        {
            int counterPart = target - nums[i];

            if(map.containsKey(counterPart))
            {

                int[] res = {map.get(counterPart), i};
                return res;
            }

            map.put(nums[i], i);
        }
        return new int[] {};
    }

    

}
