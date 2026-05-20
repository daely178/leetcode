class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> brackets {
            {']','['}, {'}','{'}, {')','('}
        };

        for(auto c : s) {
            if(brackets.count(c)) {
                if(st.empty() || brackets[c] != st.top()) {
                    return false;
                }
                st.pop();
            } else {
                st.push(c);
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