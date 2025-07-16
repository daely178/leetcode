struct Node {
    int value;
    int key;
    Node *prev;
    Node *next;
    Node(int key=0, int value=0) : key(key), value(value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
public:
    unordered_map<int, Node*> mp;
    int capacity;
    Node *head = new Node();
    Node *tail = new Node();

    LRUCache(int capacity) {
        this->capacity = capacity;
        head->next = tail;
        tail->prev =head;
    }
    
    int get(int key) {
        if(mp.find(key) == mp.end()) {
            return -1;
        }
        Node *tmp = mp[key];
        remove(tmp);
        add(tmp);

        return tmp->value;
    }
    
    void put(int key, int value) {
        if(mp.find(key) != mp.end()) {
            Node *old = mp[key];
            remove(old);
        }
        Node *node = new Node(key, value);
        add(node);
        mp[key] = node;

        if(mp.size() > this->capacity) {
            Node *first = head->next;
            remove(first);
            mp.erase(first->key);
        }
    }

    void add(Node *node) {
        Node *last = tail->prev;
        last->next = node;
        node->prev = last;
        node->next = tail;
        tail->prev = node;
    }

    void remove(Node *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);

 stack FIFO push(), pop() O(1)
 queue LIFO front(), pop(), push() O(1)
 Linked list

  2 1 3
 */