import hashlib
import os

def generate_hash(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        # Read file in chunks to save memory
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

print("--- Audio Integrity Report ---")
for file in os.listdir('.'):
    if file.endswith(('.wav', '.mp3', '.py')):
        print(f"{file}: {generate_hash(file)}")
