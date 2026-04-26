class LRUCache {
private:
    struct Node {
        Node *prev;
        Node *next;
        int value;
        int key;
        Node(int key=0, int value=0) : value(value), key(key), prev(nullptr), next(nullptr) {}
    };
    std::unordered_map<int, Node*> mp;
    int capacity;
    Node *head, *tail;


    void add(Node *node) {
        // head - last - tail
        // head - last - node - tail
        Node *last = tail->prev;
        last->next = node;
        node->prev = last;
        node->next = tail;
        tail->prev = node;
    }

    void remove(Node *node) {
        // head - prev - node - next - tail
        // head - prev - next - tail

        node->prev->next = node->next;
        node->next->prev = node->prev;

    }

public:
    LRUCache(int capacity) : capacity(capacity) {
        
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if(mp.find(key) != mp.end()) {
            Node *node = mp[key];
            remove(node);
            add(node);
            return node->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(mp.find(key) != mp.end()) {
            Node *node = mp[key];
            remove(node);
            mp.erase(key);
            delete node;
        }

        if(capacity == mp.size()) {
            Node *lru = head->next;
            remove(lru);
            mp.erase(lru->key);
            delete lru;
        }

        Node *node = new Node(key, value);
        add(node);
        mp[key] = node;        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);


least recently used, O(1)
hash map with linked to get from end and remove from start

get return key value or -1
update : remove and add to the end
put : remove existing one if exist, remove first if full then add to the end


 */