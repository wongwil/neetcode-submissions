class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not current.children[i]:
                current.children[i] = TrieNode()

            current = current.children[i]
            
        current.isEndOfWord = True


    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            i = ord(c) - ord('a')
            if current.children[i]:
                current = current.children[i]
            else:
                return False

        return current.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if current.children[i]:
                current = current.children[i]
            else:
                return False

        return True
        
        