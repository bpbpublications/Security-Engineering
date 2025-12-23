# OAuth Token Introspection Example (from manuscript)

This folder includes a reference `.http` snippet matching the RFC 7662 token introspection pattern.
Use a tool like curl or an HTTP client to adapt this to your environment.

## Request
```http
POST /introspect
Authorization: Basic base64(client_id:secret)
Content-Type: application/x-www-form-urlencoded

token=ACCESS_TOKEN
```

## Response (example)
```json
{
  "active": true,
  "scope": "read write",
  "client_id": "abc123",
  "username": "user@example.com",
  "exp": 1712129999
}
```