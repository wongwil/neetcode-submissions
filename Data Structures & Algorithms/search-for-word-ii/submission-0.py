class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEndOfWord = False
    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            
            current = current.children[c]

        current.IsEndOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTrie = Trie()
        for word in words:
            myTrie.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        res = set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r,c) in visited or
                board[r][c] not in node.children):
                return 

            
            character = board[r][c]

            node = node.children[character]
            word += character
            if node.IsEndOfWord:
                res.add(word)

            visited.add((r,c))

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, myTrie.root, "")

        return list(res)


            



