class HashTableEntry:
	"""
	Hash Table entry, as a linked list node.
	"""

	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None


class HashTable:
	"""
	A hash table that with `capacity` buckets
	that accepts string keys
	Implement this.
	"""

	def __init__(self, capacity):
		self.capacity = capacity
		self.storage = [None] * capacity
		self.load_factor = 0

	def get_load_factor(self):
		held_objects = 0
		for node in self.storage:
			if node is not None:
				held_objects += 1
		load_factor = held_objects / self.capacity
		return load_factor

	def fnv1(self, key):
		"""
		FNV-1 64-bit hash function

		Implement this, and/or DJB2.
		"""

	def djb2(self, key):
		"""
		DJB2 32-bit hash function

		Implement this, and/or FNV-1.
		"""
		hash_output = 5381  # set default hash to this number
		for char in key:  # for each character in the key
			hash_output = ((hash_output << 5) + hash_output) + ord(char)
		# shifts all bits 5 places to the left and adds the original hash to it
		# then adds to the hash the Unicode for each individual character
		return hash_output

	def hash_index(self, key):
		"""
		Take an arbitrary key and return a valid integer index
		between within the storage capacity of the hash table.
		"""
		# return self.fnv1(key) % self.capacity
		# print(self.djb2(key) % self.capacity)
		return self.djb2(key) % self.capacity

	def put(self, key, value):
		"""
		Store the value with the given key.

		Hash collisions should be handled with Linked List Chaining.

		Implement this.
		"""
		index = self.hash_index(key)  # After creating the index through the hashing algorithm
		node = self.storage[index]
		if node is None:
			self.storage[index] = HashTableEntry(key, value)  # Put the value that was passed in at that index
			return
		prev = node
		while node is not None and node.key != key:
			prev = node
			node = node.next
		if prev.key == key:
			prev.value = value
		else:
			prev.next = HashTableEntry(key, value)

	def get(self, key):
		"""
		Retrieve the value stored with the given key.

		Returns None if the key is not found.

		Implement this.
		"""
		index = self.hash_index(key)  # Find the index created through the hashing algorithm
		node = self.storage[index]
		# if node is not None:
		# 	return node.value
		while node is not None and node.key != key:
			node = node.next
		if node is None:
			return None
		else:
			return node.value

	def delete(self, key):
		"""
		Remove the value stored with the given key.

		Print a warning if the key is not found.

		Implement this.
		"""
		index = self.hash_index(key)  # Find the index for the value from the key via hashing algorithm
		self.storage[index] = None

	def resize(self):
		"""
		Doubles the capacity of the hash table and
		rehash all key/value pairs.

		Implement this.
		"""
		load_factor = self.get_load_factor()
		print(f'load factor in resize: {load_factor}')
		if load_factor > 0.7:
			print('Resizing Hash Map')
			old_storage = self.storage
			self.capacity = self.capacity * 2
			self.storage = [None] * self.capacity
			for element in old_storage:
				node = element
				while node:
					self.put(node.key, node.value)
					node = node.next


if __name__ == "__main__":
	ht = HashTable(8)

	ht.put("line_1", "Tiny hash table")
	ht.put("line_2", "Filled beyond capacity")
	ht.put("line_3", "Linked list saves the day!")

	print("")

	# Test storing beyond capacity
	print(ht.get("line_1"))
	print(ht.get("line_2"))
	print(ht.get("line_3"))

	print('')
	# Test Load Factor
	# print(ht.get_load_factor())

	# Test resizing
	old_capacity = len(ht.storage)
	ht.resize()
	new_capacity = len(ht.storage)

	print(f"\nResized from {old_capacity} to {new_capacity}.\n")

	# Test if data intact after resizing
	print(ht.get("line_1"))
	print(ht.get("line_2"))
	print(ht.get("line_3"))

	print("")