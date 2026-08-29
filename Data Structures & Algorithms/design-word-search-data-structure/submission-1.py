class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            i = ord(c) - ord('a')

            if not current.children[i]:
                current.children[i] = TrieNode()

            current = current.children[i]

        current.isEndOfWord = True


    def search(self, word: str) -> bool:
        
        def dfs(i, currentNode):
            if i == len(word):
                return currentNode.isEndOfWord

            c = word[i]

            if c == '.':
                for children in currentNode.children:
                    if children and dfs(i+1, children):
                        return True

                return False
            else:            
                idx = ord(c) - ord('a')
                if not currentNode.children[idx]:
                    return False
                else:
                    return dfs(i+1, currentNode.children[idx])

        return dfs(0, self.root)
