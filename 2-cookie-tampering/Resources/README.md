## how to find the flag

The vulnerability is a cookie tampering issue that allows privilege escalation.

The application stores the admin status in a client-side cookie named `I_am_admin`.

![cookies](cookies.png)

Its value is an MD5 hash representing a boolean value "false" (used crackstation.net for decrypting).

![crackstation decrypt hash](hash_decrypt.png)

By changing this cookie to the MD5 hash of "true", the server considers the user as an
administrator and returns the flag.

This is a security issue because cookies are fully controlled by the client and must
never be trusted for authorization decisions.

## how to avoid

This vulnerability occurs because the application relies on a client-side value to
decide whether a user is an administrator.

Hashing the value (MD5) does not provide security, because an attacker can easily
recompute the hash for any chosen value (e.g. "true") and send it to the server.

In real-world applications, this can lead to full privilege escalation, access to
restricted areas, and unauthorized actions.

To prevent this issue, authorization must be enforced server-side using sessions and
server-side checks. If a token is stored in a cookie, it must be a secure, server-issued
session identifier, and the server must determine the user's role from its own database,
not from a client-controlled value.
