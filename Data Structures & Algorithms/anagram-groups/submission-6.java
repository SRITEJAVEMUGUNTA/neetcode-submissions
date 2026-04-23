class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, ArrayList<String>> res = new HashMap<String, ArrayList<String>>();


        for(String s: strs)
        {
            char[] arr = s.toCharArray();

            Arrays.sort(arr);

            String sortedS = new String(arr);

            res.putIfAbsent(sortedS, new ArrayList<String>());

            res.get(sortedS).add(s);
        }

        return new ArrayList<>(res.values());
        
    }
}
