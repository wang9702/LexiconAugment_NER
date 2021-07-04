import collections

# 字典树
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True

    # space=''
    def enumerateMatch(self, word, space="_", backward=False):
        matched = []
        # ['中', '国', '国', '籍']
        while len(word) > 0:
            if self.search(word):
                matched.append(space.join(word[:]))
            del word[-1]
            # ['中', '国', '国']
        return matched
