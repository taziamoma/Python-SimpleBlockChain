import hashlib

class NeuralCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" +previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Taz sends 1 coin"
t2 = "Taz sends 4 coin"
t3 = "Taz sends 5.7 coin"
t4 = "Taz sends 9.0 coin"
t5 = "Taz sends 2.9 coin"
t6 = "Taz sends 8.9 coin"

init_block = NeuralCoinBlock("Initial String", [t1,t2])

print(init_block.block_data)
print(init_block.block_hash)

second_block = NeuralCoinBlock(init_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)