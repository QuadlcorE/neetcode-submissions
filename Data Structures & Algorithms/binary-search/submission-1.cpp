class Solution {
public:
    int search(vector<int>& nums, int target) {
        // We shall do it with a while loop
        int l = 0; 
        int r = nums.size()-1;
        int i;
        while (!(l>r)) {
            i = l + (r-l)/2;
            if (nums[i] == target) return i;

            if (target < nums[i]) {
                r = i-1;
            }
            else {
                l = i+1;
            }
        }
        return -1;
    }
};
