import json
import hashlib
from datetime import datetime


class Block():

	def __init__(self, index, timestamp, data, previous_hash):
		super().__init__()
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		string_to_be_hashed = str(self.index) + str(self.timestamp) + self.previous_hash + json.dumps(self.data)
		byte_string = string_to_be_hashed.encode()

		return hashlib.sha256(byte_string).hexdigest()

	def real_time(self):
		return datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')