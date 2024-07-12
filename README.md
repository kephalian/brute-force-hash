
# Brute Force MD5 Hash Matching

This Python script attempts to find the original 8-digit numbers that match given MD5 hash values. The script will hash every number in the specified range and check if it matches any of the provided MD5 hash strings.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the script.

2. Ensure you have Python 3 installed on your system.

3. Run the script using the command:

   ```sh
   python md5_brute_force.py
   ```

## Script

```python
import hashlib

# List of encoded MD5 strings to match
encoded_strings = ["2BktiRm56qr5vRT", "S242BYunQb53JWyBl2"]

def md5_hash_string(string):
    """Generate MD5 hash for a given string."""
    return hashlib.md5(string.encode()).hexdigest()

# Define N1 and N2 for 8-digit numbers
N1 = 8
N2 = N1 + 1

# Loop through the range of 8-digit numbers
for i in range(10**N1, 10**N2):
    hash_value = md5_hash_string(str(i))
    if hash_value in encoded_strings:
        print(f"Match found: {i} -> {hash_value}")
```

## Explanation

- The script defines a list of encoded MD5 hash strings in `encoded_strings`.
- The `md5_hash_string` function takes a string input and returns its MD5 hash.
- The script defines `N1` as 8 to represent 8-digit numbers.
- The script loops through all 8-digit numbers from `10**N1` to `10**N2` (10000000 to 99999999).
- For each number in the range, the script calculates its MD5 hash and checks if it matches any of the encoded strings in `encoded_strings`.
- If a match is found, it prints the original number and its hash value.

## License

This project is licensed under the MIT License 
