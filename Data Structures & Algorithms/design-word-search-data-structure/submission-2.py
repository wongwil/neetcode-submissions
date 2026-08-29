class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.isEndOfWord = True


    def search(self, word: str) -> bool:
        
        def dfs(i, currentNode):
            if i == len(word):
                return currentNode.isEndOfWord

            c = word[i]

            if c == '.':
                for children in currentNode.children.values():
                    if dfs(i+1, children):
                        return True

                return False
            else:            
                if c not in currentNode.children:
                    return False
                else:
                    return dfs(i+1, currentNode.children[c])

        return dfs(0, self.root)
