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
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Trie()
        if not board:
            return []
        for w in words:
            tree.insert(w)
        visted = [[False for j in i] for i in board]
        head_q = list()
        head_q.append((0, 0))
        visted[0][0] = True
        res = list()
        
        def in_board(r,c):
            nonlocal board
            if  r >= len(board) or  r < 0 or c >= len(board[0]) or c< 0:
                return False
            return True
        
        def slove(r,c, tmp_str,res:set, visted):
            nonlocal board
            nonlocal tree
            if tree.search(tmp_str):
                res.append(tmp_str)
            
            if in_board(r, c+1) and (not visted[r][c+1])   and tree.startsWith(tmp_str + board[r][c+1]) :
                # 下拓展
                down_visted = [[j for j in i] for i in visted]
                down_visted[r][c+1] = True
                slove(r, c+1, tmp_str + board[r][c+1], res, down_visted)
            
            if in_board(r, c-1) and (not visted[r][c-1])  and tree.startsWith(tmp_str + board[r][c-1]) :
                # 上拓展
                up_visted = [[j for j in i] for i in visted]
                up_visted[r][c-1] = True
                slove(r, c-1, tmp_str + board[r][c-1], res, up_visted)
                
            if in_board(r+1, c) and (not visted[r+1][c]) and tree.startsWith(tmp_str + board[r+1][c]):
                # 右拓展
                right_visted = [[j for j in i] for i in visted]
                right_visted[r+1][c]=True
                slove(r+1, c, tmp_str + board[r+1][c],res ,right_visted)
            
            if in_board(r-1, c)and (not visted[r-1][c]) and tree.startsWith(tmp_str + board[r-1][c]):
                # 左拓展
                left_visted = [[j for j in i] for i in visted]
                left_visted[r-1][c] = True
                slove(r-1, c, tmp_str + board[r-1][c],res ,left_visted)
              
        while head_q:
            pos = head_q.pop(0)

            tmp_str = ''
            if  tree.startsWith(board[pos[0]][pos[1]]):
                tmp_visted = [[False for j in i] for i in board]
                tmp_visted[pos[0]][pos[1]] = True
                slove(r=pos[0], c=pos[1], tmp_str=board[pos[0]][pos[1]], res=res,visted = tmp_visted)
            r= pos[0]
            c= pos[1]
            if in_board(r, c+1) and (not visted[r][c+1]):
                visted[r][c+1] = True
                head_q.append((r, c+1))
            if in_board(r+1, c) and (not visted[r+1][c]):
                visted[r+1][c] = True
                head_q.append((r+1, c))
        
        return set(res)