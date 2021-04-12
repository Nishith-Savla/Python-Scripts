class MovieNode:
	def __init__(self, movie_name, rel_date):
		self.movie_name = movie_name
		self.rel_date = rel_date
		self.next = None

		
class MovieLinkedList:
	def __init__(self):
		self.head = None

	def add_to_start(self, movie_name, rel_date):
		new_node = MovieNode(movie_name, rel_date)
		if not self.head:
			self.head = new_node
			return None
		new_node.next = self.head
		self.head = new_node
		return None

	def pop(self):
		if not self.head:
			print("No movies to delete")
			return -1

		second_last_node = last_node = None
		movie_node = self.head

		while(movie_node):
			second_last_node = last_node
			last_node = movie_node
			movie_node = movie_node.next

		second_last_node.next = None

	def display_movie_list(self):
		if not self.head:
			print('No movies to show right now')
			return 
		
		movie_node = self.head
		while(movie_node):
			print(f"{movie_node.movie_name} {movie_node.rel_date} => ", end="")
			movie_node = movie_node.next
		print(None)


movie_list = MovieLinkedList()
movie_list.add_to_start('Movie 1', 'd1/m1/yyy1')
movie_list.add_to_start('Movie 2', 'd2/m2/yyy2')
movie_list.add_to_start('Movie 3', 'd3/m3/yyy3')
movie_list.display_movie_list()
movie_list.pop()
movie_list.display_movie_list()
