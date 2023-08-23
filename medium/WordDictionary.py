'''
211. Design Add and Search Words Data Structure
Medium
7.1K
407
Companies
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''   

from collections import defaultdict
from typing import List


class WordDictionary:
        
    def __init__(self):
        self.worddict = defaultdict(set)

    def addWord(self, word: str) -> None:
        length = len(word)        
        self.worddict[length].add(word) 

    def search(self, word: str) -> bool:
        length = len(word)
        if '.' not in self.worddict[length]:
            return word in self.worddict[length]

        for word_s in self.worddict[length]:
            for i, ch in enumerate(word_s):
                if word[i] != '.' and word[i] != ch:
                    break
            else:
                return True
        return False
    
class TrieNode:
    def __init__(self):
        self.isword = False
        self.children = {}

class WordDictionaryTrie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isword = True
        
    def node_search(self, node, word, index):
        
        if index == len(word):
            return node.isword

        c = word[index]
        if c == '.':
            for child in node.children.values():
                if self.node_search(child, word, index+1):
                    return True
        else:
            if c in node.children:
                return self.node_search(node.children[c], word, index+1)
            else:
                return False            
            
    def search(self, word: str) -> bool:                
        return self.node_search(self.root, word, 0)            

    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

funclist = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
keylist =  [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output [null, null, true, false, true, null, true]

#Explanation

wordDictionary = WordDictionaryTrie()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.addWord("bxc")
wordDictionary.search("pad") # return False
wordDictionary.search("bad") # return True
wordDictionary.search(".ad") # return True
wordDictionary.search("b..") # return True
print(wordDictionary.search("b.c")) # return True


# key points
# 1. lower case English letters in add word
# 2. '.' in search word dots can be matched with any letter
# 3. return Boolean if search() can find the word
# 4. at most 10exp4 calls

# Strategy
# 1. Tree per single char
# 2. dictionary vs list
# 3. dfs search vs iteration
# 4. dot handling

# 1. Tree structure
#    root
#   b    d  m
#   a x  a  a 
#   d c  d  d

# 2. dictionary
# key value

# 3. hash
# key value

# 4. stack, q not appropriate