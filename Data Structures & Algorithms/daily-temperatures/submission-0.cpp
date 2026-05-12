class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // vector of value : location
        std::stack<std::pair<int, int>> seen;
        int n = temperatures.size();
        std::vector<int> result(n, 0);

        for (int i = 0; i<n; i++) {
            // We want to push to the stack but first check that what is on the stack is smaller than then pop
            // if smaller than curr pop from stack and add it's result.
            int curr = temperatures[i];
            while (!seen.empty() && seen.top().first < curr) {
                result[seen.top().second] = i-seen.top().second;
                seen.pop();
            }
            seen.push({curr, i});
        }
        return result;
    }
};
