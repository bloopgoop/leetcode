class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.equals("")) {
            return true;
        }
        if (t.equals("")) {
            return false;
        }

        int slow = 0;
        for (int fast = 0; fast < t.length(); fast++) {
            if (s.charAt(slow) == t.charAt(fast)) {
                slow++;
            }
            if (slow == s.length()) {
                return true;
            }
        }
        return false;
    }
}