# Smart solution with a few new things to learn

# dict.setdefault(c, {}) --> if it doesn't exist then create an entry
# dict.pop("key", False) --> if key exists in dictionary, then return value and remove the entry
#                        --> if key doesn't exist return the default value in second parameter
# complex numbers for grid exploration
# some trie optimizations
# when creating trie, create a count of how many times a node is passed in creation
# then when a word is found, decrement the count and traverse back up the tree
# so that when a node's count is 0, you can stop traversal
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        grid = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                grid[i + j*1j] = board[i][j]
        
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node["endsHere"] = True
        
        result = []
        def dfs(node, spot, currWord):
            if node.pop("endsHere", False):
                result.append(''.join(currWord))
            
            currChar = grid.get(spot, None)
            # see if there is a word that can continue it
            if currChar in node:
                grid[spot] = "$" # make sure the same letter can't be reused
                currWord.append(currChar)
                for i in range(4):
                    dfs(node[currChar], spot + (1j)**i, currWord)
                currWord.pop()
                grid[spot] = currChar
        
        for spot in grid:
            dfs(root, spot, [])
        
        return result
        
                
        
        