class Solution {
public:
    string simplifyPath(string path) {
        int n = path.length();
        int i = 0;
        stack<string> st;

        for(int i=0; i<n; i++){
            if(path[i] == '/'){
                continue;
            }

            string temp;
            while(i<n && path[i] != '/'){
                temp += path[i++];
            }
            if(temp == ".")
                continue;
            else if(temp == ".."){
                if(!st.empty()){
                    st.pop();
                }
            }
            else {
                st.push(temp);
            }
        }

        string res = "";
        while(!st.empty()){
            res = "/" + st.top() + res;
            st.pop();
        }
        if(res.length() == 0)
            return "/";
        return res;
    }
};

/*
    patterns
    remove last '/'
    ../ -> parent
    ... valid name directory
    /./ can be removed

    stack<string> st
    forward while loop

        if not . or /
*/