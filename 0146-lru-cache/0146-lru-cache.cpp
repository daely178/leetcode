struct Node{
    int key;
    int value;
    Node *prev;
    Node *next;
    Node(int key=0, int value=0) : key(key), value(value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity_ = capacity;
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
        Node *tmp = new Node(key, value);
        mp[key] = tmp;
        add(tmp);

        if(mp.size() > capacity_) {
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
private:
    int capacity_;
    std::unordered_map<int, Node*> mp;
    Node *head = new Node();
    Node *tail = new Node();
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */


 /*

get() 
return existing value for the key
make it latest

put()
insert value if key doesn't exist
update value if key exist
make it the latest

0(1)

Find key should be using map()
double linked list to insert/remove/add to manage items with O(1)

 */