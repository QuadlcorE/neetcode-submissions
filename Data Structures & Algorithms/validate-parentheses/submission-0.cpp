class Solution {
public:
    bool isValid(string s) {
        std::vector<char> stack;
        for (auto character: s) {
            std::cout << "Here as well: " << character << std::endl;
            if (character == '(' || character == '{' || character == '[') {
                stack.push_back(character);
                std::cout << "Pushed" << std::endl;
            }
            else if ( !stack.empty() && (
                    (character == ')' && stack.back() == '(') || 
                    (character == '}' && stack.back() == '{') ||
                    (character == ']' && stack.back() == '['))
            ) {
                stack.pop_back();
                std::cout << "Popped"<< std::endl;
            } else return false;
        }
        if (stack.empty()) return true;
                return false;
    }
};
