class LRUCache {
private:
    struct Node {
        int val;
        int key;
        Node *prev;
        Node *next;
        Node(int key=0, int val=0) : key(key), val(val), prev(nullptr), next(nullptr) {}
    };    
    unordered_map<int, Node*> mp;    
    int capacity;
    Node *head;
    Node *tail;
    void remove(Node *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
    void addToFront(Node *node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;        
    }
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if(mp.find(key) == mp.end()) {
            return -1;
        }

        // cache update
        Node *node = mp[key];
        remove(node);
        addToFront(node);

        return node->val;
    }
    
    void put(int key, int value) {
        if(mp.find(key) != mp.end()) {
            Node *node = mp[key];
            node->val = value;
            remove(node);
            addToFront(node);
            return;
        }
        if(capacity == mp.size()) {
            Node *lruNode = tail->prev;
            remove(lruNode);            
            mp.erase(lruNode->key);
            delete lruNode;
        }
        Node *newNode = new Node(key, value);
        addToFront(newNode);
        mp[key] = newNode;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);

 O(1) put/get

struct Node {
    int val;
    Node *prev;
    Node *next;
    Node(int val=0, Node *p=nullptr, Node *n=nullptr) : val(val), prev(p), next(n);
};

 unordered_map<Node*, Node*> mp;
 */