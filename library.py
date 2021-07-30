import os
import re

class Library:
	def __init__(self):
		self._secret_key = os.environ.get("SECRET_LIB_KEY") 
		self._books_list = ['The man who laughs', 'Metro-2033', 'White Fang', 'The Amphibian']


	@staticmethod
	def get_books():
		if os.environ.get("SECRET_LIB_KEY") is None:
			return "Forbidden action"
		else:
			return self._books_list

	@staticmethod
	def give_book(book_name):
		get_books()
		if book_name is None:
			return f"Can't give this book {book_name} to you", False
		else:
			self._books_list.remove(book_name)
			return self._books_list


	@staticmethod
	def check_student_key(pub_key):
		pub_key = os.environ.get("STUDENT_PUB_KEY")
		pattern = re.compile(r"[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{6}")
		try:
			re.match(pattern, pub_key)
			print("Public Key Success")
			return True
		except None:
			print("Wrong Public Key")
			return False







