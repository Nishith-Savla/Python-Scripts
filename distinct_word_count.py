"""Find the number of distinct words in a string."""

def get_word_count():
	"""Get the word from the user and prints the count of distinct words as well as count of each word."""
	n_words = int(input("Enter the total number of words: "))
	print("Enter the words: ")

	words = []
	for _ in range(n_words):
		words.append(str(input()))
	
	# Calculate
	distinct_words, each_word_count = distinct_word_count(words)
	
	# Display the output
	print(distinct_words)
	for word_count in each_word_count:
		print(word_count, end=" ")


def distinct_word_count(words: list[str]) -> tuple[int, tuple[int]]:
	"""Count the number of distinct words in the list.

	Parameters
	==========
	words: list[str]
		The list of words to count.
	
	Returns
	=======
	len(word_count), word_count.values(): tuple[int, tuple[int]]
		A tuple containing the number of distinct words and list of occurences of words.
	"""
	word_count = {}
	for word in words:  # Counting occurences of each word
		word_count[word] = word_count.get(word, 0) + 1

	return len(word_count), word_count.values()


if __name__ == '__main__':
	get_word_count()
