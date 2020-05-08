from hashtable import HashTable, HashTableEntry
import unittest


def get_indices_of_item_weights(weights, length, limit):
	"""
	Create Hash Table
	Add each entry to hash table
	Find higher value
	If there is a higher value, return it
	If pair does not exist, return None
	"""
	hash_table = HashTable(16)

	for i in range(length):
		hash_table.put(weights[i], i)
	for j in range(length):
		greater = hash_table.get(limit - weights[j])
		if greater:
			return greater, j
		else:
			return None


def test_ex1_1():
	weights_3 = [4, 6, 10, 15, 16]
	answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
	print(f'answer_3 {answer_3}')

test_ex1_1()
