# APPROACH  
# Time Complexity : Total insert operations - O(mn) m: number of words inserted, n: average length of the words, Each search and startswith operation - O(m) 
# Space Complexity : O(nm) - space of trie
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Each trie node had Boolean end flag and array of 26 children ( 1 for each letter lowercase)
# 2. To insert a word, start searching from the root, and proceed with each letter of the word and the corresponding children of the node. If the node is empty at a particular 
#    char, then insert a new node at that index and proceed till the last char of the word. 
# 3. Similarly for search and startswith operation. If anywhere the node is None at a particular index, return False as the word / prefix doesn't exist. For search, at the 
#    end check if the boolean End is True or not. For startswith, no such check is required. 

class Node:
    def __init__(self):
        self.isEnd = False
        self.children = [None for _ in range(26)]
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root
        for char in word:
            if curr_node.children[ord(char) - ord('a')] is None:
                curr_node.children[ord(char) - ord('a')] = Node()
            curr_node = curr_node.children[ord(char) - ord('a')]
        curr_node.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.root
        for char in word:
            if curr_node.children[ord(char) - ord('a')] is None:
                return False
            curr_node = curr_node.children[ord(char) - ord('a')]
        if curr_node.isEnd:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.root
        for char in prefix:
            if curr_node.children[ord(char) - ord('a')] is None:
                return False
            curr_node = curr_node.children[ord(char) - ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
