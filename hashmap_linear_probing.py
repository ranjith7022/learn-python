class HashMap:
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and original_index == index:
                raise Exception("hashmap is full")
            first_iteration = False
            index = (index + 1) % len(self.hashmap)

        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        while True:
            if self.hashmap[index] is None:
                return None  # Key not found (empty slot)

            if not first_iteration and original_index == index:
                return None  # Key not found (probed entire array)
            first_iteration = False

            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]

            index = (index + 1) % len(self.hashmap)

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