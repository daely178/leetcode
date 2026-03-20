
class Solution {
public:
    int calculate(string s) {
        char op = '+';
        stack<int> st;
        long num = 0;
        for(int i=0; i<s.size(); i++) {
            char c = s[i];
            
            if( c >= '0' && c <= '9') {
                num = num*10 + c - '0';
            }

            if(c == '-' || c== '*' || c=='/' || c=='+' || i==(s.size()-1)) {
                if(op == '-') {
                    st.push(-num);
                } else if(op == '+') {
                    st.push(num);
                }else if(op == '*') {
                    int tmp = num*st.top();
                    st.pop();
                    st.push(tmp);
                }else if(op == '/') {
                    int tmp = st.top()/num;
                    st.pop();
                    st.push(tmp);
                }
                op = c;
                num = 0;
            } 

        }

        int ret = 0;
        while(!st.empty()) {
            ret += st.top();
            st.pop();
        }

        return ret;
    }
};

/*
given expression is valid
integer range result

integers to push to stack
operand

    stack
        + 
           num
*/
