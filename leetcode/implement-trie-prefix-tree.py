class TrieNode:
    def __init__(self, val):
        self.val = val
        self.word = False
        self.node = {}
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pre = self.root
        for w in word:
            if pre.node.get(w) is None:
                pre.node[w] = TrieNode(w)
            pre = pre.node[w]
        pre.word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pre = self.root
        for w in word:
            if pre.node.get(w) is None:
                return False
            else:
                pre = pre.node[w]
        if not pre.word:
            return False
        return True
        
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pre = self.root
        for w in prefix:
            if pre.node.get(w) is None:
                return False
            else:
                pre = pre.node[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)