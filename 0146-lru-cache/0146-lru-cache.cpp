struct Node{
    int key;
    int value;
    Node *prev;
    Node *next;
    Node(int key, int value) : key(key), value(value), prev(nullptr), next(nullptr){}
};
class LRUCache {
public:
    int capacity;
    unordered_map<int, Node*> mp;
    Node *head = new Node(-1,-1);
    Node *tail = new Node(-1,-1);

    LRUCache(int capacity){
        this->capacity = capacity;
        head->next= tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if(mp.find(key) == mp.end()){
            return -1;
        }
        Node *node = mp[key];
        remove(node);
        add(node);
        return node->value;
    }
    
    void put(int key, int value) {
        Node *old = nullptr;
        if(mp.find(key) != mp.end()){
            old = mp[key];
            remove(old);
        }
        if(old != nullptr) {
            old->key = key;
            old->value = value;
        }
        else {
            old = new Node(key, value);
        }
        mp[key] = old;
        add(old);

        if(mp.size() > this->capacity) {
            Node *delNode = head->next;
            remove(delNode);
            mp.erase(delNode->key);
        }
    }

    void add(Node *node){
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
 */