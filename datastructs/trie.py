# example trie storing a few words
words = ['apple', 'app', 'amazon','kid']

# each node has children nodes list, marker for if it is the end of a word, and a character
class TrieNode:
    def __init__(self, c):
        self.nodes = {}
        self.isWord = False
        self.chr = c
    
    def __repr__(self):
        children_repr = ", ".join(repr(n) for n in self.nodes.values())
        return f"{self.chr} [{children_repr}]"
    

# build it with dict
def hashmapBuildTrie(words):
    root = TrieNode("")
    for w in words:
        p = root
        for c in w:
            if c not in p.nodes:
                p.nodes[c] = TrieNode(c)
            p = p.nodes[c]
        p.isWord = True
    return root

# returns the root node of a trie containing the words
# def buildTrie(words):
#     root = TrieNode("")
#     for w in words:
#         p = root
#         for c in w:
#             if len(p.nodes) == 0:
#                 # create new node
#                 newNode = TrieNode(c)
#                 p.nodes.append(newNode)
#                 p = newNode
#             else:
#                 foundIn = False
#                 for n in p.nodes:
#                     if c == n.chr:
#                         p = n
#                         foundIn = True
#                         break
#                 if not foundIn:
#                     # create new node
#                     newNode = TrieNode(c)
#                     p.nodes.append(newNode)
#                     p = newNode
#         p.isWord = True
#     return root

# r = buildTrie(words)
# print(r)

r2 = hashmapBuildTrie(words)
print(r2)