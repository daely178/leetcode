
class Solution {
public:
    int calculate(string s) {
        char op = '+';
        long temp = 0;
        std::stack<int> st;

        for(int i=0; i<s.size(); i++) {
            const char c = s[i];
            if(c >= '0' && c <= '9') {
                temp = temp*10 + c-'0';
            }

            if(c == '+' || c == '-' || c == '*' || c == '/' || i==(s.size()-1)) {

                if(op == '+') {
                    st.push(temp);
                } else if ( op == '-') {
                    st.push(-temp);
                } else if( op == '*') {
                    int top = st.top();
                    st.pop();
                    st.push(top*temp);
                } else if(op == '/') {
                    int top = st.top();
                    st.pop();
                    st.push(top/temp);
                }
                op = c;
                temp = 0;
            }
        }

        int res = 0;
        while(!st.empty()) {
            res += st.top();
            st.pop();
        }

        return res;
    }
};

/*

initial op = +
stack
3
2
* or / pop() * or / then push
*/
