# validate_id_token.py
# Demonstrates issuing and verifying a JWT (ID token-like) locally.
# In production, you would fetch the JWKS from the IdP's discovery document.
#
# Usage: python validate_id_token.py

import time
import json
from typing import Dict
import jwt
from jwt import PyJWKClient
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

ISSUER = "https://login.example.com"
AUDIENCE = "my-client-id"

def generate_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def to_pem_keys(private_key, public_key):
    priv_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pub_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return priv_pem, pub_pem

def issue_id_token(private_key) -> str:
    now = int(time.time())
    payload = {
        "iss": ISSUER,
        "aud": AUDIENCE,
        "sub": "user123",
        "email": "alex@example.com",
        "exp": now + 300,
        "iat": now,
        "nonce": "random-nonce-123",
    }
    token = jwt.encode(payload, private_key, algorithm="RS256")
    return token

def verify_id_token(token: str, public_key_pem: bytes) -> Dict:
    data = jwt.decode(
        token,
        public_key_pem,
        algorithms=["RS256"],
        audience=AUDIENCE,
        issuer=ISSUER,
    )
    return data

if __name__ == "__main__":
    priv, pub = generate_keypair()
    priv_pem, pub_pem = to_pem_keys(priv, pub)
    token = issue_id_token(priv_pem)
    print("Issued ID Token:", token)
    claims = verify_id_token(token, pub_pem)
    print("Verified claims:", json.dumps(claims, indent=2))