class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<string> stack;
        for (auto token: tokens) {
            if (token == "+" ||
                token == "-" ||
                token == "*" ||
                token == "/"
            ) {
                // We want to take the last two numbers from the stack and use the operand on them then push them back unto the stack. 
                // Do we have to validate the input being given?
                int rightoperand = std::stoi(stack.back());
                stack.pop_back();
                int leftoperand = std::stoi(stack.back());
                stack.pop_back();
                int result;

                if (token == "+") result = leftoperand + rightoperand;
                else if (token == "-") result = leftoperand - rightoperand;
                else if (token == "*") result = leftoperand * rightoperand;
                else if (token == "/") result = leftoperand / rightoperand;

                stack.push_back(std::to_string(result));
            } 
            else stack.push_back(token);
        }
        return std::stoi(stack.back());
    }
};
