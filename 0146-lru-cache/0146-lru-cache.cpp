struct Node {
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {}
};

class LRUCache {
public:
    int capacity;
    unordered_map<int, Node*> dic;
    Node *head = new Node(-1, -1);
    Node *tail = new Node(-1, -1);
    LRUCache(int capacity) {
        this->capacity = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if(dic.find(key) == dic.end()) {
            return -1;
        }
        Node *node = dic[key];
        remove(node);
        add(node);
        return node->val;
    }
    
    void put(int key, int value) {
        Node *old = nullptr;
        if(dic.find(key) != dic.end()){
            Node *old = dic[key];
            remove(old);
        }

        if(old != nullptr){
            old->val = value;
            old->key = key;
        }
        else {
            old = new Node(key, value);
        }
        dic[key] = old;
        add(old);

        if(dic.size() > capacity) {
            Node *nodeToDel = head->next;
            remove(nodeToDel);
            dic.erase(nodeToDel->key);
        }
    }

    void add(Node* node)
    {
        Node *prevEnd = tail->prev;
        prevEnd->next = node;
        node->prev = prevEnd;
        node->next = tail;
        tail->prev = node;
    }

    void remove(Node* node){
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