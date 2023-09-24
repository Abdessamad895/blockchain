from Blockchain import Blockchain

def main():
    # Créer une instance de la blockchain
    my_blockchain = Blockchain()

    # Ajouter quelques blocs à la blockchain
    my_blockchain.add_block("Première transaction")
    my_blockchain.add_block("Deuxième transaction")
    my_blockchain.add_block("Troisième transaction")

    # Afficher la blockchain
    for block in my_blockchain.chain:
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print()

if __name__ == "__main__":
    main()
