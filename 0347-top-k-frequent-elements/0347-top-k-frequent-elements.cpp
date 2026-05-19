class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        auto comp = [](const pair<int,int>& a, const pair<int,int>& b) { return a.first > b.first; };

        using MinHeap = priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(comp)>;

        for(auto num : nums) {
            freq[num]++;
        }

        MinHeap minHeap;
        for(auto& [num, count] : freq) {
            minHeap.push({count, num});
            if(minHeap.size() > k) {
                minHeap.pop();
            }
        }

        vector<int> result;
        while(!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return result;
    }
};

/*
heap
map <int,int> key, count

priority_queue<
*/