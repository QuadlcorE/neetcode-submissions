class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # So we need to just search through the whole array for each letter of the word. 
        # We just need to return true if the word is in the board.
        # We do not need to store any values or locations
        # Are there alphabetic characters? 
        # Doesn't matter comparison in python of different types is possible, would just return False

        # Firstly I need a to cycle through the whole board to find the first character. 
        # When I find this char I perform some sort of DFS to find if the word can be found. 
        # I have to remember to keep the search within the borders of the board.

        # We also need to keep track of visited squares
        seen = set()

        # We need a search function that can check if the curr location is the same as the curr letter in the word
        def search(x, y, curr):
            # Our base cases firstly
            # Make sure we haven't seen this loc before
            if (x, y) in seen:
                return False
            # We need to find out if we've reached the end of the word.
            if curr >= len(word):
                return True
            # We need out of bound checks.
            if x<0 or x>=len(board) or y<0 or y>= len(board[0]):
                return False
            
            letter = word[curr]
            loc = board[x][y]
            if loc != letter:
                return False
            
            seen.add((x, y))
            status = search(x-1, y, curr+1) or search(x+1, y, curr+1) or search(x, y+1, curr+1) or search(x, y-1, curr+1)
            seen.remove((x, y))
            return status
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if search(x, y, 0):
                    return True
        
        return False