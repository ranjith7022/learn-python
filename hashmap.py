class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap)== 0:
            self.hashmap.append(None)
        if self.current_load()<0.05:
            return
        temp = self.hashmap
        size = len(self.hashmap)
        self.hashmap = [None for i in range(size*10)]
        for i in temp:
            if i is not None:
                print(i)
                self.hashmap[self.key_to_index(i[0])] = (i[0],i[1]) 

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        return sum(1 for i in self.hashmap if i is not None)/ len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
