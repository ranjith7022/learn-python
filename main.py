class Trie:
    def find_matches(self, document):
        matches = set()
        current = self.root
        for i in document:
            for j in current:
                pass
                
            
            

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
