# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] == None:
            self.storage[hashed_key] = LinkedPair(key, value)
        else: 
            newLinkedPair = LinkedPair(key, value)
            newLinkedPair.next = self.storage[hashed_key]
            self.storage[hashed_key] = newLinkedPair
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] == None:
            print('Key is not found')
        else: 
            previousKey = None
            currentKey = self.storage[hashed_key]

            #loop through the list. Find the Matching list item. 
            while currentKey:
                if currentKey.key == key:
                    #remove the matching list item
                    print('key matched, removing item')
                    #patch the list. 
                    if currentKey.next != None: 
                        if previousKey == None: 
                            #first item in list match. 
                            self.storage[hashed_key] = currentKey.next
                            return
                        else: 
                            previousKey.next = currentKey.next
                            return
                    else:
                        #last item in list match. 
                        if previousKey == None:
                            #only item in list case. 
                            self.storage[hashed_key] = None
                            return
                        else: 
                        #previous key pointer now points to none. effectively removing the item from the list. 
                            previousKey.next = None
                            return
                else: 
                    #previous key must equal current key so it is the previous key
                    previousKey = currentKey
                    #current key does not match, lets move to next item in array. 
                    currentKey = currentKey.next
            print("key not found")





    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        currentKey = self.storage[hashed_key]

        while currentKey:
            if currentKey.key != key:
                currentKey = currentKey.next
            else:
                return currentKey.value
        return None
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht)
    print("")
