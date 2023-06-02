import hashlib
import os

# Define your string
your_string = "Denver in 6"

# Create an MD5 hash
md5_hash = hashlib.md5(your_string.encode()).hexdigest()

# Create a SHA1 hash
sha1_hash = hashlib.sha1(your_string.encode()).hexdigest()

# Create a SHA256 hash
sha256_hash = hashlib.sha256(your_string.encode()).hexdigest()

# Create a new directory if it doesn't exist
hashes2hashes_dir = 'hashes'
if not os.path.exists(hashes2hashes_dir):
    os.makedirs(hashes2hashes_dir)

# Save the hash values in a file inside the new directory
with open(os.path.join(hashes2hashes_dir, 'hashes.txt'), 'w') as f:
    f.write(f"MD5 Hash: {md5_hash}\n")
    f.write(f"SHA1 Hash: {sha1_hash}\n")
    f.write(f"SHA256 Hash: {sha256_hash}\n")

print(f"Hash values saved in {hashes2hashes_dir}/hashes.txt")

