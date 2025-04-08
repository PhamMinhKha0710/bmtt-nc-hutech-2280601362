import hashlib

def blake2b(message):
    blake2b_hash = hashlib.blake2b(digest_size=64)
    blake2b_hash.update(message)
    return blake2b_hash.digest()

def main():
    text = input("Nhap du lieu can hash: ").encode('utf-8')
    hash_value = blake2b(text)

    print("chuoi van ban da nhap:", text.decode('utf-8'))
    print("hash blake2b:", hash_value.hex())

if __name__ == "__main__":
    main()
