class Solution {
    public int compress(char[] chars) {
        int left = 0;
        int right = 0;
        int write_ptr = 0;

        while (right < chars.length) {
            if (chars[left] == chars[right]) {
                right++;
            } else {
                // write current consecutive character to the array then increment write_ptr
                chars[write_ptr++] = chars[left];

                // write count of current consecutive character to the array
                if ((right - left) > 1) {
                    for (char digit : Integer.toString(right - left).toCharArray()) {
                        chars[write_ptr++] = digit;
                    }
                }
                left = right;
            }
        }

        // perform last compression if necessary
        chars[write_ptr++] = chars[left];
        if ((right - left) > 1) {
            for (char digit : Integer.toString(right - left).toCharArray()) {
                chars[write_ptr++] = digit;
            }
        }

        //System.out.println(Arrays.toString(chars));

        // return length of new array
        return write_ptr;
    }
}