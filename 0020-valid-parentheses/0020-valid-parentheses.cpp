class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for(auto c : s) {
            if(c == '(' || c == '[' || c == '{') {
                st.push(c);
            }
            if(c == ']' || c == ')' || c == '}') {
                if(st.empty()) {
                    return false;
                }
                char opened = st.top();
                if( (c == ']' && opened == '[') ||
                    (c == '}' && opened == '{') ||
                    (c == ')' && opened == '(') ) {
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
()
1. map : '[' : ']'
2. stack open
3. check stack top if close
*/