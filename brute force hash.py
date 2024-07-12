import hashlib

encoded_strings = ["2BktiRm56qr5vRT", "S242BYunQb53JWyBl2"]

def md5_hash_string(string):
    return hashlib.sha1(string.encode()).hexdigest()
#Number or Digits in the Decoded string
N1=6
N2=N1+1
# 8 digit number like 12345678
# Assuming we are looking for 6-digit numbers
for i in range( 10**N1, 10**N2):
    hash_value = md5_hash_string(str(i))
    if hash_value in encoded_strings:
        print(f"Match found: {i} -> {hash_value}")
        exit()
    
print("No match found")