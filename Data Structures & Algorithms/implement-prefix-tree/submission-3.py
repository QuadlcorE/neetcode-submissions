class TreeNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.head = TreeNode("")

    def insert(self, word: str) -> None:
        cur = self.head
        for l in word:
            if l in cur.children:
                cur = cur.children[l]
                continue
            newNode = TreeNode(l)
            cur.children[l] = newNode
            cur = newNode
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.head
        for l in word:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return True if cur.end == True else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for l in prefix:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return True
        