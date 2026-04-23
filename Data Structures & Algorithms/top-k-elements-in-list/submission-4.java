class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int num: nums)
        {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> heap = new PriorityQueue<>((a,b) -> a[0] - b[0]);

        for(int num: map.keySet())
        {
            heap.add(new int[] {map.get(num), num});

            if(heap.size() > k)
            {
                heap.poll();
            }

        }

        int[] res = new int[k];

        for(int i = 0; i < k; i++)
        {
            res[i] = heap.poll()[1];
        }

        return res;

    }
}
