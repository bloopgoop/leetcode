class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }

        // strings are the same structure, so find the GCD using Euclidean algorithm
        int gcd_len = gcd(str1.length(), str2.length());
        return str1.substring(0, gcd_len);
    }

    /**
    Function finds gcd(a, b) where a >= b
    */
    private int gcd(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}