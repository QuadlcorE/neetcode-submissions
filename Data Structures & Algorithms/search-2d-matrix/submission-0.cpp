class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // we have to search rows first by checking if a value is within the range of the values and check. 
        int upper_limit = 0;
        int lower_limit = matrix.size()-1;
        int curr_row;

        while (!(upper_limit>lower_limit)) {
            curr_row = upper_limit + (lower_limit-upper_limit)/2;
            // check if value is within current value range.
            if (target <= matrix[curr_row].back() && target >= matrix[curr_row][0]) {
                // we search the curr_row
                int start = 0;
                int end = matrix[curr_row].size() -1;
                int curr;
                while(!(start>end)) {
                    curr = start + (end-start)/2;
                    if (target == matrix[curr_row][curr]) return true;
                    if (target < matrix[curr_row][curr]) end = curr -1;
                    else start = curr +1;
                }
            }
            if (target < matrix[curr_row][0]) lower_limit = curr_row -1;
            else upper_limit = curr_row +1;
        }
        return false;
    }
};
