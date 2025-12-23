# bcrypt_example.py
# Runnable example based on the manuscript's bcrypt snippet.
# Hash a password and then verify it.
# Usage: python bcrypt_example.py

import bcrypt

def hash_password(pw: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw.encode("utf-8"), salt)

def verify_password(pw: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(pw.encode("utf-8"), hashed)

if __name__ == "__main__":
    password = "SecureP@ssw0rd!"
    hashed = hash_password(password)
    print("Hashed:", hashed.decode())
    print("Verify correct:", verify_password("SecureP@ssw0rd!", hashed))
    print("Verify wrong:", verify_password("wrong", hashed))