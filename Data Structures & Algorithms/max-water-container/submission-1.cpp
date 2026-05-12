class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size()-1;
        int maxvol = 0;
        while (l<r) {
            int vol = std::min(heights[l], heights[r]) * (r-l);
            maxvol = std::max(vol, maxvol);
            if (heights[l] < heights[r]) l++;
            else r--;
        }
        return maxvol;
    }
};
