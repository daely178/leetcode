'''
208. Implement Trie (Prefix Tree)
Medium
10.7K
120
Companies
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''   

from typing import List


class Trie:
    
    class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.endOfWord = False     
        
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        
        length = len(word)
        TrieRoot = self.root
        lst = []
        lst.extend(word)
        for ch in lst:
            charIndex = ord(ch) - ord('a')
            if not TrieRoot.children[charIndex]:
                TrieRoot.children[charIndex] = self.TrieNode()
            TrieRoot = TrieRoot.children[charIndex]
        TrieRoot.endOfWord = True

    def search(self, word: str) -> bool:
        
        length = len(word)
        TrieRoot = self.root
        lst = list(word)
        for ch in lst:
            charIndex = ord(ch) - ord('a')
            if not TrieRoot.children[charIndex]:
                return False
            TrieRoot = TrieRoot.children[charIndex]        
        
        return TrieRoot.endOfWord

    def startsWith(self, prefix: str) -> bool:
        
        length = len(prefix)
        TrieRoot = self.root
        lst = list(prefix)
        for ch in lst:
            charIndex = ord(ch) - ord('a')
            if not TrieRoot.children[charIndex]:
                return False
            TrieRoot = TrieRoot.children[charIndex]        
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

funclist = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"] 
keylist =  [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output [null, null, true, false, true, null, true]

#Explanation
trie = Trie()

print(trie.insert("a"))
print(trie.search("a"))
#print(trie.search("app"))
print(trie.startsWith("a"))
#print(trie.insert("app"))
#print(trie.search("app"))

