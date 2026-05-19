class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;

        for(int i=0; i<n; i++) {
            
            int j=i+1;
            int k=n-1;

            if(nums[i] > 0) {
                break;
            }
            if(i>0 && nums[i] == nums[i-1]) {
                continue;
            }

            while(j<k) {
                int subSum = nums[j]+nums[k];

                if(subSum + nums[i] > 0) {
                    k--;
                } else if (subSum + nums[i] < 0) {
                    j++;
                } else {
                    result.push_back({nums[i], nums[j], nums[k]});

                    while(j<k && nums[j] == nums[j+1]) j++;
                    while(j<k && nums[k] == nums[k-1]) k--;

                    j++;
                    k--;                    
                }
            }            
        }    
        return result;    
    }
};

/*
int n=num.size()
sort(nums.begin(), nums.end())
vector<vector<int>> result;

for(int i=0; i<n; i++) {
    
    int j=i+1;
    int k=n-1;

    if(nums[i] > 0) {
        break;
    }
    if(i>0 && nums[i] == nums[i-1]) {
        continue;
    }

    int target = nums[i];
    while(j<k) {
        int subSum = nums[j]+nums[k];

        if(subSum - nums[i] > 0) {
            j++;
        } else if (subSum - nums[i] < 0) {
            k--;
        } else {
            result.push_back({nums[i], nums[j], nums[k]});

            while(j<k && nums[j] == nums[j+1]) j++;
            while(j<k && nums[k] == nums[k-1]) k--;
        }

        j++;
        k--;
    }
    return result;
}



*/