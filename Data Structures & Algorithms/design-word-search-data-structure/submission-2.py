class TreeNode:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.head = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        # I feel like this should be a recursive function
        # Return true if the length of word is 1 and that char is in child of the curr node
        def check(root, curr_word):
            cur = root

            for i, char in enumerate(curr_word):
                # Check the wild card solution
                if char == ".":
                    for child in cur.children.values():
                        if check(child, curr_word[i+1:]):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.end
        
        return check(self.head, word)