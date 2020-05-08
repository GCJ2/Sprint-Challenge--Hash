def intersection(arrays):
	cache = {}
	returns = []

	for array in arrays:                        # Arrays are nested, so we need to loop through each of them
		for number in array:                    # For each number in each array
			if number not in cache:             # If it's not in the cache
				cache[number] = 1               # Add it with a value of 1
			elif number in cache:               # If it's already in the cache
				cache[number] += 1              # Increment it's value by 1
			if cache[number] == len(arrays):    # If the value of an item in the cache is equal to the number of nested arrays
				returns.append(number)          # That means it's in all the arrays, so we add it to the list of returns
	print(returns)
	return returns

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
