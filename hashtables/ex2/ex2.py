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
	ht = HashTable(length)          # Create hash table with size from length
	route = []                  # Create the route list that will be taken and returned

	for i in range(len(tickets)):   # Loop over tickets
		if tickets[i].source == 'NONE':     # Find the ticket who's source is NONE
			beginning = tickets[i].destination  # Set that to the beginning of the trip
		ht.put(tickets[i].source, tickets[i].destination)   # Add all other tickets to the ht

	for i in range(len(tickets)):   # Loop back over length of tickets
		if i == 0:                  # At index 0
			route.append(beginning)     # Add that to the list, as it is our leaving point
		else:
			ticket = ht.get(route[i-1])     # Otherwise, set ticket subsequent item in ht
			route.append(ticket)            # And add it to our route list

	return route
