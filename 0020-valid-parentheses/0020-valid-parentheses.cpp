class Solution {
public:
    bool isValid(string s) {

        std::stack<char> st;

        for(const auto c : s) {
            if(c == '{' || c == '[' || c == '(') {
                st.push(c);
            } else if(c == '}' || c == ']' || c == ')') {
                if( !st.empty() &&
                   ((c == '}' && st.top() == '{') ||
                   (c == ']' && st.top() == '[') ||
                   (c == ')' && st.top() == '(')) ) {
                    st.pop();
                } else {
                    return false;
                }
            }
        }
        if(!st.empty()) {
            return false;
        }
        return true;
    }
};

/*

()[]{}

if open, push to stack
if close, check stack top

*/