import hashlib
import time
class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(data.encode()).hexdigest()