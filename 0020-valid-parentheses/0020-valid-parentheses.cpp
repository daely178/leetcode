class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st;
        
        for(char c : s) {
            if(c == '{' || c == '[' || c == '(') {
                st.push(c);
            } else if( c == '}' || c == ']' || c== ')'){
                if (!st.empty() &&
                    (st.top() == '{' && c == '}'||
                    st.top() == '[' && c == ']' ||
                    st.top() == '(' && c == ')' ) ){
                    st.pop();
                } else {
                    return false;
                }
            }
        }

        return st.empty();
        /*
            { [ ( push to stack
            } ] ) check stack and pop
            check stack size == 0 at the end
        */
    }
};