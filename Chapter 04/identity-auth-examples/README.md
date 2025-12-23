# Identity & Authentication – Executable Examples

This repository packages runnable code extracted and engineered from your manuscript chapter so the publisher can push it to GitHub.

## How to run
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python python/bcrypt_example.py
python python/totp_example.py
python oidc/validate_id_token.py
```

## Structure
- `python/bcrypt_example.py` – Password hashing & verification with bcrypt (Chapter section: Password-based authentication). See citations below.
- `python/totp_example.py` – TOTP generation & verification with PyOTP (Chapter section: MFA / TOTP). See citations below.
- `oidc/validate_id_token.py` – Local OIDC-style ID token sign & verify with RS256 to demonstrate validation logic.
- `oauth/README.md`, `oauth/introspect_example.http` – RFC 7662 token introspection request/response patterns.
- `requirements.txt` – Python dependencies.

## Manuscript → Code Mapping (Citations)
- bcrypt example derived from the manuscript's snippet (lines referenced): fileciteturn1file0L21-L45 / fileciteturn1file2L87-L111
- TOTP example derived from the manuscript's PyOTP snippet: fileciteturn1file0L135-L166
- OAuth introspection request/response mirrored from the manuscript: fileciteturn1file3L179-L233
- WebAuthn workflow and terminology referenced for future extensions: fileciteturn1file4L5-L20

## Notes
- The OIDC example is fully runnable using a locally generated keypair to illustrate ID token validation (signature, iss, aud, exp checks). In production, load keys from the provider's JWKS.
- If you want Dockerized examples or GitHub Actions CI, we can add them.