# totp_example.py
# Runnable example using pyotp (TOTP) based on the manuscript.
# Usage: python totp_example.py
#
# It prints a secret and the current OTP. Run again within 30s and verify.

import time
import pyotp

def generate_secret() -> str:
    return pyotp.random_base32()

def current_otp(secret: str) -> str:
    return pyotp.TOTP(secret).now()

def verify_otp(secret: str, user_otp: str) -> bool:
    return pyotp.TOTP(secret).verify(user_otp)

if __name__ == "__main__":
    secret = generate_secret()
    print("Secret:", secret)
    otp = current_otp(secret)
    print("Current OTP:", otp)
    # Simulate user entry
    time.sleep(1)
    ok = verify_otp(secret, otp)
    print("Verification result:", ok)