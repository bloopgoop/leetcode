class Solution {
    public String reverseVowels(String s) {
        char[] word = s.toCharArray();
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (isVowel(word[l]) && isVowel(word[r])) {
                /* System.out.println("l=" + l + ", word[l]=" + word[l] + ", isVowel=" + isVowel(word[l]) + 
                   ", r=" + r + ", word[r]=" + word[r] + ", isVowel=" + isVowel(word[r]));
                */
                char temp = word[l];
                word[l] = word[r];
                word[r] = temp;

                l++;
                r--;
            } else if (isVowel(word[l])) {
                r--;
            } else if (isVowel(word[r])) {
                l++;
            } else {
                l++;
                r--;
            }
        }
        return new String(word);
    }

    private boolean isVowel(char c) {
        return (c == 'a'
            || c == 'e' 
            || c == 'i' 
            || c == 'o' 
            || c == 'u' 
            || c == 'A' 
            || c == 'E'
            || c == 'I'
            || c == 'O'
            || c == 'U');
    }
}