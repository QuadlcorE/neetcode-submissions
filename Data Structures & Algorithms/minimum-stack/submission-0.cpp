struct paired {
    int value{};
    int maxSeen{};
};

class MinStack {
public:
    std::vector<paired> seen;
    MinStack() {
        
    }
    
    void push(int val) {
        int currMax;
        if (seen.empty()) {
            currMax = val;
        }
        else {
            currMax = std::min(seen.back().maxSeen, val);
        }
        paired newTop{val, currMax};
        seen.push_back(newTop);
    }
    
    void pop() {
        if (!seen.empty()) seen.pop_back();
    }
    
    int top() {
        if (!seen.empty()) {
            return seen.back().value;
        }
        else return NULL;
    }
    
    int getMin() {
        if (!seen.empty()) return seen.back().maxSeen;
        else return NULL;
    }
};
