#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtable import HashTable


class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination


def reconstruct_trip(tickets, length):
	"""
	YOUR CODE HERE
	"""
	ht = HashTable(length)
	route = [None] * length

	for i in range(len(tickets)):
		if tickets[i].source == 'NONE':
			beginning = tickets[i].destination
		ht.put(tickets[i].source, tickets[i].destination)

	route = []

	for i in range(len(tickets)):
		if i == 0:
			route.append(beginning)
		else:
			ticket = ht.get(route[i-1])
			route.append(ticket)

	return route
