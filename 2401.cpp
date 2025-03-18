#include <iostream>
#include <vector>
class Solution {
    public:
        int longestNiceSubarray(vector<int>& nums) {
            int maxLen = 1;
            for (int i = 0; i < nums.size(); i++) {
                int bitMask = 0;
                for (int j = i; j < nums.size(); j++){
                    if ((bitMask & nums[j]) != 0) {
                        break;
                    }
                    bitMask |= nums[j];
                    maxLen = max(maxLen, j-i+1);
                }
            }
            return maxLen;
        }
        // for every value in the array
        //      check it against another value in the array AND if it = 0
        //      add it to the new array
        // output array
    
    };