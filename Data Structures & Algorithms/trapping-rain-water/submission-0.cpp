class Solution {
public:
    int trap(vector<int>& height) {
        int arrsize = height.size();
        if (arrsize == 0) return 0;
        vector<int> leftmax(arrsize, 0);
        vector<int> rightmax(arrsize, 0);

        leftmax[0] = height[0];
        for (int i=1; i<arrsize; i++) {
            leftmax[i] = std::max(height[i], leftmax[i-1]);
        }

        rightmax[arrsize-1] = height[arrsize-1];
        for (int i=arrsize-2; i>-1; i--) {
            rightmax[i] = std::max(height[i], rightmax[i+1]);
        }

        int total = 0;
        for (int i=0; i<arrsize; i++) {
            int curvol = std::min(leftmax[i], rightmax[i]) - height[i];
            if (curvol > 0 ) total += curvol;
        }
        return total;
    }
};
