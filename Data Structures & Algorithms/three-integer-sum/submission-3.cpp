class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); i++) {
            // We know the array is sorted so if nums[i] > 0 we can't have any numbers less than 0 to give 0
            if (nums[i] > 0) break;
            // We want to initialize l and r pointers and count 
            if (i>0 && nums[i] == nums[i-1]) {
                // we want to continue but increase i
                continue;
            }
            int l = i+1;
            int r = nums.size() -1;
            while (l<r) {
                // We wanna check if the sum == 0 
                int summ = nums[i] + nums[l] + nums[r];
                if (summ < 0 ) l++;
                else if (summ > 0 ) r--;
                else if (summ == 0) {
                    vector<int> tmp {nums[i], nums[l], nums[r]};
                    result.push_back(tmp);
                    l++;
                    r--;
                    while (nums[l] == nums[l-1] && l < r) l++;
                }
            }
        }
        return result;
    }
};
