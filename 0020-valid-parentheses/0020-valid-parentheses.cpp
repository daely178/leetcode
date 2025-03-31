class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for(char c : s) {
            if(c=='{'||c=='('||c=='['){
                st.push(c);
            } else if(!st.empty()){
                char pc = st.top();
                if( (c=='}' && pc != '{') ||
                    (c==']' && pc != '[') ||
                    (c==')' && pc != '(') )
                    return false;
                st.pop();
            }
            else
                return false;
        }
        return st.empty();
    }
};