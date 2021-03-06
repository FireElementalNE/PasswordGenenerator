from typing import List

from utils import rand_int

class Alphabet:
	def __init__(self, length: int):
		self.length = length

	def get_random_char(self) -> str:
		x: int = rand_int()
		valid_chars: List[int] = [chr(el) for el in 
		[	48, 49, 50, 51, 52, 53, 54, 55, 56, 
			57, 33, 34, 35, 36, 37, 38, 40, 41, 
			42, 43, 44, 45, 46, 58, 59, 60, 61, 
			62, 63, 64, 65, 66, 67, 68, 69, 70, 
			71, 72, 73, 74, 75, 76, 77, 78, 79, 
			80, 81, 82, 83, 84, 85, 86, 87, 88, 
			89, 90, 97, 98, 99, 100, 101, 102, 103, 
			104, 105, 106, 107, 108, 109, 110, 111, 
			112, 113, 114, 115, 116, 117, 118, 119, 
			120, 121, 122 ] ]

		return valid_chars[x % len(valid_chars)]

	def get_password(self) -> str:
		out_str: List[str] = []
		for i in range(self.length):
			out_str.append(self.get_random_char())
		return ''.join(out_str)
		