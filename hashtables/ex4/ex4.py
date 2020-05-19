def has_negatives(a):
	cache = {}
	returns = []

	for number in a:
		if number not in cache:                 # If the number is not in the cache
			if number > 0:                      # If the number is also greater than 0
				cache[number] = number          # Add it to the cache with a + in front
			elif number < 0:                    # If the number is negative
				cache[-number] = number         # Set it in cache with negative as key and positive as value
		if number > 0:                          # If number is in cache and greater than 1
			if -number in cache:                # And has it's negative equivalent in the cache
				returns.append(number)          # Add it to the return list
		if number < 0:                          # If number is in the cache and less than 1
			if -number in cache:                # Check for positive equivalent by canceling out negative
				returns.append(-number)         # Add it to the return list
	print(cache)
	return returns
	# print(returns)

if __name__ == "__main__":
	print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
