# Class created for the Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
class Chaining_Hash_Table:
    # Creates buckets with an empty list and initializes them to 0.
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts or updates an item into the hash table.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def insert(self, key, item):
        # Obtains the bucket list where the item will go into.
        bucket_object = hash(key) % len(self.table)
        bucket_list = self.table[bucket_object]

        # Updates key if already present in bucket.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # If it is not present, inserts it into the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with a matching key in the hash table.
    # Returns the object if it is in the hash table, otherwise returns None.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def search(self, key):
        # Finds the bucket list where the key would be located.
        bucket_object = hash(key) % len(self.table)
        bucket_list = self.table[bucket_object]

        # Searches for the key within the bucket list.
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Looks up a specific attribute in the hash table from a key and the attribute that the user is searching for.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lookup(self, key, lookup_value):
        # Finds the bucket list where the key would be located.
        bucket_object = hash(key) % len(self.table)
        bucket_list = self.table[bucket_object]
        lv = lookup_value

        # Searches for the key within the bucket list and returns the corresponding attribute that is also searched for.
        for kv in bucket_list:
            if kv[0] == key:
                if hasattr(kv[1], lv):
                    if lv == "packageID":
                        return kv[1].packageID
                    if lv == "address":
                        return kv[1].address
                    if lv == "city":
                        return kv[1].city
                    if lv == "state":
                        return kv[1].state
                    if lv == "zipCode":
                        return kv[1].zipCode
                    if lv == "deliveryDeadline":
                        return kv[1].deliveryDeadline
                    if lv == "mass":
                        return kv[1].mass
                    if lv == "specialNotes":
                        return kv[1].specialNotes
                    if lv == "status":
                        return kv[1].status
                    if lv == "timestamp":
                        return kv[1].timestamp
                return "Package attribute not valid."
        return None

    # Removes an item with matching key from the hash table.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def remove(self, key):
        # Obtains the bucket list where this item will be removed from.
        bucket_object = hash(key) % len(self.table)
        bucket_list = self.table[bucket_object]

        # Removes the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])