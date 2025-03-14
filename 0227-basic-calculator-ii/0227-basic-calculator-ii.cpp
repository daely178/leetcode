
class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        int n = s.length();
        char op = '+';
        long tmp = 0, res = 0;
        for(int i=0; i<n; i++) {
            if(isdigit(s[i])){
                tmp = tmp*10 + s[i]-'0';
            }
            if(!isdigit(s[i]) && !iswspace(s[i]) || i==n-1) {
                if(op == '-') {
                    st.push(-tmp);
                }
                else if(op == '+'){
                    st.push(tmp);
                }
                else {
                    int num = 0;
                    if(op == '*') {
                        num = st.top()*tmp;
                    }
                    else {
                        num = st.top()/tmp;
                    }
                    st.pop();
                    st.push(num);
                }
                op = s[i];
                tmp = 0;
            }
        }
        while(!st.empty()){
            res += st.top();
            st.pop();
        }
        return res;
    }
};
