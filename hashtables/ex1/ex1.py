from hashtable1 import HashTable, hash_table_retrieve, hash_table_insert
import unittest


def get_indices_of_item_weights(weights, length, limit):
	"""
	Create Hash Table
	Add each entry to hash table
	Find higher value
	If there is a higher value, return it
	If pair does not exist, return None
	"""

	# Had to use a different hash table here to due an error I could not figure out

	# hash_table = HashTable(16)
	#
	# for i in range(length):
	# 	hash_table.put(str(weights[i]), i)
	# for j in range(length):
	# 	greater = hash_table.get(limit - weights[j])
	# 	if greater:
	# 		return greater, j
	# 	else:
	# 		return None

	ht = HashTable(16)

	for i in range(length):                     # Only go to range of length passed in
		hash_table_insert(ht, weights[i], i)    # Insert node into hash table as new hash table

	for j in range(length):                     # Second loop through length
		greater = hash_table_retrieve(ht, limit - weights[j])   # Goes through ht to find greater index
		if greater:                             # If it exists
			return greater, j                   # Return it and what is found there
