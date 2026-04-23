class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();
        
        for(let x = 0; x < nums.length; x++) {
            const comp = target - nums[x];

            if(map.has(comp)) {
                return [map.get(comp), x];
            }

            map.set(nums[x], x);
        }

        return [];
    }
}
